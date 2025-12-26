#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DERIN CLI - Command Line Interface
===================================

Derin'i terminal'den kontrol et.

Kullanım:
    derin status        # Sistem durumu
    derin logs          # Son loglar
    derin health        # Sağlık kontrolü
    derin backup        # Manuel backup
    derin people        # Tanıdığı kişiler
    derin news          # Bugünün haberleri
"""

import sys
import argparse
from pathlib import Path

# Derin root'u ekle
sys.path.insert(0, str(Path(__file__).parent.parent))


def cmd_status():
    """Sistem durumu"""
    from core.autonomous_manager import get_autonomous_manager
    
    print("\n" + "="*60)
    print("DERIN v20.0 - System Status")
    print("="*60)
    
    manager = get_autonomous_manager()
    status = manager.get_status()
    
    print(f"\nInitialized: {'Yes' if status['initialized'] else 'No'}")
    print(f"Running services: {status['running_services']}")
    
    # Night optimization
    if status.get('night_optimization') != "Not available":
        nsi = status['night_optimization']
        print(f"\nNight Optimization:")
        print(f"  Scheduler: {'Active' if nsi.get('scheduler_running') else 'Inactive'}")
        print(f"  Is night time: {'Yes' if nsi.get('is_night_time') else 'No'}")
        if nsi.get('last_analysis'):
            print(f"  Last run: {nsi['last_analysis'].get('date', 'N/A')}")
    
    # Backup
    if status.get('backup') != "Not available":
        backup = status['backup']
        print(f"\nBackup:")
        print(f"  Total backups: {backup.get('total_backups', 0)}")
        print(f"  Latest: {backup.get('latest_backup', 'None')}")
        print(f"  Size: {backup.get('total_size_mb', 0):.1f}MB")
        print(f"  Scheduler: {'Active' if backup.get('scheduler_running') else 'Inactive'}")
    
    print()


def cmd_logs(lines=20):
    """Son logları göster"""
    from core.life_logger import get_life_logger
    
    print("\n" + "="*60)
    print(f"DERIN - Last {lines} Log Entries")
    print("="*60 + "\n")
    
    try:
        logger = get_life_logger()
        events = logger.get_recent_events(lines)
        
        for event in events[-lines:]:
            timestamp = event.get('timestamp', 'N/A')
            event_type = event.get('type', 'unknown')
            summary = event.get('summary', 'No summary')
            
            print(f"[{timestamp}] {event_type.upper()}")
            print(f"  {summary[:80]}")
            print()
            
    except Exception as e:
        print(f"Error: {e}")


def cmd_health():
    """Sağlık kontrolü"""
    import psutil
    import torch
    
    print("\n" + "="*60)
    print("DERIN - Health Check")
    print("="*60)
    
    # CPU
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"\nCPU: {cpu_percent}%")
    
    # Memory
    mem = psutil.virtual_memory()
    print(f"RAM: {mem.percent}% ({mem.used/1024**3:.1f}GB / {mem.total/1024**3:.1f}GB)")
    
    # GPU
    if torch.cuda.is_available():
        print(f"\nGPU: {torch.cuda.get_device_name(0)}")
        print(f"VRAM: {torch.cuda.memory_allocated()/1024**3:.1f}GB / {torch.cuda.get_device_properties(0).total_memory/1024**3:.1f}GB")
        
        # Temperature (if available)
        try:
            import pynvml
            pynvml.nvmlInit()
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
            print(f"GPU Temp: {temp}°C")
        except:
            pass
    
    # Disk
    disk = psutil.disk_usage('/')
    print(f"\nDisk: {disk.percent}% ({disk.used/1024**3:.1f}GB / {disk.total/1024**3:.1f}GB)")
    
    print()


def cmd_backup():
    """Manuel backup oluştur"""
    from core.automated_backup import get_automated_backup
    
    print("\n" + "="*60)
    print("DERIN - Creating Backup")
    print("="*60 + "\n")
    
    backup = get_automated_backup()
    manifest = backup.create_backup()
    
    print(f"Backup created: {manifest['timestamp']}")
    print(f"Targets: {', '.join(manifest['targets'])}")
    print(f"Size: {manifest['total_size_bytes']/1024/1024:.2f}MB")
    print(f"Duration: {manifest['duration_seconds']:.1f}s")
    print()


def cmd_people():
    """Tanıdığı kişiler"""
    from personality.multi_user_manager import get_multi_user_manager
    
    print("\n" + "="*60)
    print("DERIN - People I Know")
    print("="*60 + "\n")
    
    manager = get_multi_user_manager()
    people = manager.list_all_people()
    
    if not people:
        print("No one registered yet.")
        return
    
    for person in people:
        print(f"{person.name}")
        print(f"  Relationship: {person.relationship.value}")
        print(f"  Interactions: {person.total_interactions}")
        print(f"  Interests: {', '.join(person.interests[:3])}")
        print()


def cmd_news():
    """Bugünün haberleri"""
    from core.daily_news_absorption import get_daily_news
    
    print("\n" + "="*60)
    print("DERIN - Today's News")
    print("="*60 + "\n")
    
    news = get_daily_news()
    print(news.get_todays_summary())
    print()


def main():
    parser = argparse.ArgumentParser(
        description="DERIN CLI - Control your AI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # status
    subparsers.add_parser('status', help='System status')
    
    # logs
    logs_parser = subparsers.add_parser('logs', help='Recent logs')
    logs_parser.add_argument('-n', '--lines', type=int, default=20, help='Number of lines')
    
    # health
    subparsers.add_parser('health', help='Health check')
    
    # backup
    subparsers.add_parser('backup', help='Create backup')
    
    # people
    subparsers.add_parser('people', help='List people')
    
    # news
    subparsers.add_parser('news', help="Today's news")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Route commands
    if args.command == 'status':
        cmd_status()
    elif args.command == 'logs':
        cmd_logs(args.lines)
    elif args.command == 'health':
        cmd_health()
    elif args.command == 'backup':
        cmd_backup()
    elif args.command == 'people':
        cmd_people()
    elif args.command == 'news':
        cmd_news()


if __name__ == '__main__':
    main()
