"""
DERİN v20.0 - Central Nervous System (CNS)
═══════════════════════════════════════════
Ana orkestratör. Tüm biyolojik modülleri koordine eder.
Moshi-style full-duplex, biyolojik ritim ve DNA sistemi.

v20.0: Multi-Model Manager (Thor için) + Autonomous Systems
"""

import sys
import time
import signal
import threading
import os
from colorama import init, Fore, Style

# Colorama başlat
init()

# Windows console encoding fix (Thor'da gerek yok ama zarar vermez)
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        # Python < 3.7
        pass

print(f"""
{Fore.CYAN}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     DERİN v20.0 - AUTONOMOUS DIGITAL INDIVIDUAL              ║
║     Multi-Model AI System                                     ║
║     NVIDIA Jetson AGX Thor                                    ║
║                                                               ║
║     "Makine değil, Organizma."                               ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
""")

# AUTONOMOUS SYSTEMS BAŞLAT (YENI)
print(f"{Fore.GREEN}[AUTONOMOUS] Starting background systems...{Style.RESET_ALL}")
try:
    from core.autonomous_manager import start_autonomous_systems
    start_autonomous_systems()
    print(f"{Fore.GREEN}[AUTONOMOUS] All systems operational ✓{Style.RESET_ALL}\n")
except Exception as e:
    print(f"{Fore.RED}[AUTONOMOUS] Warning: {e}{Style.RESET_ALL}\n")

class DerinCNS:
    """Merkezi Sinir Sistemi - Ana Orkestratör"""
    
    def __init__(self):
        self._running = False
        self._threads = []
        
        # Temel Modüller (v8.0)
        self._event_bus = None
        self._dna = None
        self._hypothalamus = None
        self._brainstem = None
        self._temporal = None
        self._occipital = None
        self._frontal = None
        self._broca = None
        self._limbic = None
        self._hippocampus = None
        
        # v10.1 İnsansı Modüller
        self._brain_integration = None
        self._parallel_perception = None
        self._meta_cognition = None
        self._episodic_memory = None
        
        # v10.2 Chappie/Finch Modüller
        self._eye_contact = None
        self._conversational_gestures = None
        self._smooth_motion = None
        self._continuous_vision = None
        self._stereo_coordination = None
        
        # v11.0 İnsansı Bilinç
        self._consciousness = None
        
        # v16.1 Yeni Modüller (Bugün eklendi)
        self._voice_emotion = None
        self._spontaneous_behavior = None
        self._goal_executor = None
        self._body_awareness = None
        self._audio_reflex = None
        
        # v20.0: Multi-Model Manager (Thor için)
        self._model_manager = None
    
    def _load_models_staged(self):
        """
        Aşamalı model yükleme - Thor için optimize.
        Modeller teker teker yüklenir, memory spike önlenir.
        """
        print(f"{Fore.CYAN}[MODEL] Aşamalı model yükleme başlıyor...{Style.RESET_ALL}")
        
        try:
            from core.multi_model_manager import get_multi_model_manager
            self._model_manager = get_multi_model_manager(platform="thor")
            
            # Yükleme sırası (öncelik sırasına göre)
            load_order = [
                ("reflex", "Qwen-3B", "Hızlı tepkiler için"),
                ("social", "Qwen-8B", "Sohbet için"),
                ("social_plus", "Qwen-14B", "Detaylı sohbet için"),
                ("cortical", "Qwen-70B", "Derin düşünme için"),
                # Coder modelleri lazy-load - sadece kod sorgusu gelince
            ]
            
            for i, (layer, model_name, description) in enumerate(load_order, 1):
                print(f"{Fore.YELLOW}[{i}/{len(load_order)}] {model_name} yükleniyor... ({description}){Style.RESET_ALL}")
                try:
                    self._model_manager.load_model(layer)
                    print(f"{Fore.GREEN}    └── {model_name} yüklendi{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}    └── {model_name} yüklenemedi: {e}{Style.RESET_ALL}")
                
                # Her model arasında kısa bekleme (memory stabilizasyonu)
                time.sleep(1)
            
            # KV Cache Manager başlat
            try:
                from core.kv_cache_manager import get_kv_cache_manager
                self._kv_cache = get_kv_cache_manager()
                print(f"{Fore.GREEN}[MODEL] KV Cache Manager aktif{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.YELLOW}[MODEL] KV Cache: {e}{Style.RESET_ALL}")
            
            # Hierarchical Brain başlat
            try:
                from core.hierarchical_brain import HierarchicalBrain
                self._hierarchical_brain = HierarchicalBrain()
                print(f"{Fore.GREEN}[MODEL] Hierarchical Brain aktif{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.YELLOW}[MODEL] Hierarchical Brain: {e}{Style.RESET_ALL}")
            
            print(f"{Fore.GREEN}[MODEL] Tüm modeller hazır{Style.RESET_ALL}")
            
        except Exception as e:
            print(f"{Fore.RED}[MODEL] Model yükleme hatası: {e}{Style.RESET_ALL}")
    
    def boot(self):
        """Sistemi başlat - Boot Sequence"""
        print(f"{Fore.YELLOW}[CNS] Boot sequence başlatılıyor...{Style.RESET_ALL}")
        
        # 0. DI Container (Servis Yönetimi)
        print(f"{Fore.CYAN}[0/15] DI Container...{Style.RESET_ALL}")
        from core.container import setup_core_services, get_container
        self._container = setup_core_services()
        print(f"{Fore.GREEN}    └── {len(self._container.get_all())} servis kaydedildi{Style.RESET_ALL}")
        
        # 1. Event Bus (Sinir Ağı)
        print(f"{Fore.CYAN}[1/15] Event Bus...{Style.RESET_ALL}")
        from core.event_bus import get_event_bus
        self._event_bus = get_event_bus()
        self._event_bus.start()
        
        # 2. DNA (Kimlik)
        print(f"{Fore.CYAN}[2/15] DNA...{Style.RESET_ALL}")
        from core.system.dna import get_identity, get_dna
        identity = get_identity()
        self._dna = get_dna()
        print(f"{Fore.GREEN}    └── İsim: {identity.name}{Style.RESET_ALL}")
        
        # 3. Brainstem (Refleksler)
        print(f"{Fore.CYAN}[3/15] Brainstem...{Style.RESET_ALL}")
        from core.system.brainstem import get_brainstem
        self._brainstem = get_brainstem()
        
        # 4. Hypothalamus (Biyoloji)
        print(f"{Fore.CYAN}[4/15] Hypothalamus...{Style.RESET_ALL}")
        from core.system.hypothalamus import get_hypothalamus
        self._hypothalamus = get_hypothalamus()
        self._hypothalamus.start()
        self._threads.append(self._hypothalamus)
        
        # 5. Hippocampus (Hafıza)
        print(f"{Fore.CYAN}[5/15] Hippocampus...{Style.RESET_ALL}")
        from core.memory.hippocampus import get_hippocampus
        self._hippocampus = get_hippocampus()
        
        # 6. Limbic (Duygular)
        print(f"{Fore.CYAN}[6/15] Limbic System...{Style.RESET_ALL}")
        from core.lobes.limbic import get_limbic
        self._limbic = get_limbic()
        
        # 7. Broca (Konuşma)
        print(f"{Fore.CYAN}[7/15] Broca Area...{Style.RESET_ALL}")
        from core.lobes.broca import get_broca
        self._broca = get_broca()
        self._broca.start()
        self._threads.append(self._broca)
        
        # Brainstem callback'leri kaydet
        self._brainstem.register_stop_audio(self._broca.stop_audio)
        
        # 8. Frontal (Beyin)
        print(f"{Fore.CYAN}[8/15] Frontal Lobe...{Style.RESET_ALL}")
        from core.lobes.frontal import get_frontal
        self._frontal = get_frontal()
        self._frontal.start()
        self._threads.append(self._frontal)
        
        # Brainstem callback
        self._brainstem.register_abort_generation(self._frontal.abort_generation)
        
        # 9. Temporal (Kulak) + Occipital (Göz)
        print(f"{Fore.CYAN}[9/15] Sensory Lobes...{Style.RESET_ALL}")
        from core.lobes.temporal import get_temporal
        from core.lobes.occipital import get_occipital
        
        self._temporal = get_temporal()
        self._temporal.start()
        self._threads.append(self._temporal)
        
        self._occipital = get_occipital()
        self._occipital.start()
        self._threads.append(self._occipital)
        
        # ═══════════════════════════════════════════════════════════════
        # v10.1 İNSANSI MODÜLLER
        # ═══════════════════════════════════════════════════════════════
        
        # 10. Brain Integration (Modül Entegrasyonu)
        print(f"{Fore.CYAN}[10/15] Brain Integration...{Style.RESET_ALL}")
        try:
            from core.brain_integration import get_brain_integration
            self._brain_integration = get_brain_integration()
            # Modülleri bağla
            self._brain_integration.connect_modules(
                limbic=self._limbic,
                hypothalamus=self._hypothalamus,
                episodic=self._episodic_memory,  # Aşağıda yüklenecek
                meta=self._meta_cognition  # Aşağıda yüklenecek
            )
            print(f"{Fore.GREEN}    └── Beyin entegrasyonu aktif{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}    └── Hata: {e}{Style.RESET_ALL}")
        
        # 11. Meta-Cognition (Öz-farkındalık)
        print(f"{Fore.CYAN}[11/15] Meta-Cognition...{Style.RESET_ALL}")
        try:
            from core.meta_cognition import get_meta_cognition
            self._meta_cognition = get_meta_cognition()
            print(f"{Fore.GREEN}    └── Öz-farkındalık aktif{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}    └── Hata: {e}{Style.RESET_ALL}")
        
        # 12. Episodic Memory (Yaşam Boyu Anılar)
        print(f"{Fore.CYAN}[12/15] Episodic Memory...{Style.RESET_ALL}")
        try:
            from core.episodic_memory import get_episodic_memory
            self._episodic_memory = get_episodic_memory()
            print(f"{Fore.GREEN}    └── Episodik hafıza aktif{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}    └── Hata: {e}{Style.RESET_ALL}")
        
        # Brain Integration'a geç yüklenen modülleri bağla
        if self._brain_integration:
            self._brain_integration.connect_modules(
                episodic=self._episodic_memory,
                meta=self._meta_cognition
            )
        
        # ═══════════════════════════════════════════════════════════════
        # v11.0 İNSANSI BİLİNÇ - Spontan Davranış Sistemi
        # ═══════════════════════════════════════════════════════════════
        print(f"{Fore.CYAN}[12.5/15] Human-Like Consciousness...{Style.RESET_ALL}")
        try:
            from core.consciousness import HumanLikeBrain
            self._consciousness = HumanLikeBrain()
            
            # Callback'leri bağla
            self._consciousness.set_callbacks(
                visual_callback=lambda: self._occipital.get_latest() if self._occipital and hasattr(self._occipital, 'get_latest') else None,
                action_callback=lambda text: self._event_bus.publish(
                    "AI_SPEECH_TEXT",
                    {"text": text, "is_spontaneous": True},
                    source="consciousness"
                ) if self._event_bus else None
            )
            
            self._consciousness.start()
            self._threads.append(self._consciousness)
            print(f"{Fore.GREEN}    └── Bilinç akışı ve spontan davranış aktif{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}    └── Bilinç: {e}{Style.RESET_ALL}")
        
        # ═══════════════════════════════════════════════════════════════
        # v13.0 EMERGENT ORGANIC AI - Faz 9 Modülleri
        # Kişilik, dürtüler, değerler, rasyonellik, kimlik
        # ═══════════════════════════════════════════════════════════════
        print(f"{Fore.CYAN}[12.6/15] Emergent Organic AI...{Style.RESET_ALL}")
        self._emergent_ai = None
        self._self_improvement = None
        
        try:
            from core.emergent_organic_ai import get_emergent_ai
            self._emergent_ai = get_emergent_ai()
            self._emergent_ai.start()
            print(f"{Fore.GREEN}    └── Ortaya çıkan kişilik aktif{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}    └── Emergent AI: {e}{Style.RESET_ALL}")
        
        try:
            from core.self_improvement_coordinator import get_self_improvement_coordinator
            self._self_improvement = get_self_improvement_coordinator()
            self._self_improvement.start()
            print(f"{Fore.GREEN}    └── Öz-geliştirme sistemi aktif{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}    └── Self-Improvement: {e}{Style.RESET_ALL}")
        
        # ═══════════════════════════════════════════════════════════════
        # v18.0 FAZ 1 MODÜLLERİ - Kişilik, Dürtüler, Kimlik, Değerler
        # ═══════════════════════════════════════════════════════════════
        print(f"{Fore.CYAN}[12.7/15] FAZ 1 Kognitif Modüller...{Style.RESET_ALL}")
        faz1_loaded = 0
        try:
            from core.emergent_personality import get_personality
            _ = get_personality()
            faz1_loaded += 1
        except: pass
        try:
            from core.intrinsic_drives import get_drives
            _ = get_drives()
            faz1_loaded += 1
        except: pass
        try:
            from core.autonomous_identity import get_identity as get_autonomous_identity
            _ = get_autonomous_identity()
            faz1_loaded += 1
        except: pass
        try:
            from core.learned_values import get_values
            _ = get_values()
            faz1_loaded += 1
        except: pass
        print(f"{Fore.GREEN}    └── {faz1_loaded}/4 kognitif modül yüklendi{Style.RESET_ALL}")
        
        # ═══════════════════════════════════════════════════════════════
        # v18.0 FAZ 5-7 MODÜLLERİ - Context Bridge, Goals, Self-Model
        # ═══════════════════════════════════════════════════════════════
        print(f"{Fore.CYAN}[12.8/15] FAZ 5-7 Entity Modülleri...{Style.RESET_ALL}")
        faz5_7_loaded = 0
        
        # FAZ 5: Context Bridge
        try:
            from core.context_bridge import get_context_bridge
            self._context_bridge = get_context_bridge()
            faz5_7_loaded += 1
            print(f"{Fore.GREEN}    └── ContextBridge: Cross-model context aktif{Style.RESET_ALL}")
        except Exception as e:
            self._context_bridge = None
            print(f"{Fore.YELLOW}    └── ContextBridge: {e}{Style.RESET_ALL}")
        
        # FAZ 6: Persistent Goals
        try:
            from core.goal_manager import get_goal_manager
            self._goal_manager = get_goal_manager()
            goals_count = len(self._goal_manager.get_active())
            faz5_7_loaded += 1
            print(f"{Fore.GREEN}    └── GoalManager: {goals_count} aktif hedef (persistent){Style.RESET_ALL}")
        except Exception as e:
            self._goal_manager = None
            print(f"{Fore.YELLOW}    └── GoalManager: {e}{Style.RESET_ALL}")
        
        # FAZ 7: Self-Model
        try:
            from core.self_model import get_self_model
            self._self_model = get_self_model()
            caps = self._self_model.get_stats()["enabled_capabilities"]
            faz5_7_loaded += 1
            print(f"{Fore.GREEN}    └── SelfModel: {caps} yetenek aktif (persistent){Style.RESET_ALL}")
        except Exception as e:
            self._self_model = None
            print(f"{Fore.YELLOW}    └── SelfModel: {e}{Style.RESET_ALL}")
        
        print(f"{Fore.GREEN}    └── {faz5_7_loaded}/3 entity modül yüklendi{Style.RESET_ALL}")
        
        # ═══════════════════════════════════════════════════════════════
        # v10.2 CHAPPIE/FINCH MODÜLLER
        # ═══════════════════════════════════════════════════════════════
        
        # 13. Smooth Motion (Akıcı Hareket)
        print(f"{Fore.CYAN}[13/15] Smooth Motion...{Style.RESET_ALL}")
        try:
            from robotics.smooth_motion import get_smooth_motion
            self._smooth_motion = get_smooth_motion()
            self._smooth_motion.start()
            print(f"{Fore.GREEN}    └── Akıcı hareket aktif (60 FPS){Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}    └── Hata: {e}{Style.RESET_ALL}")
        
        # 14. Continuous Vision (Sürekli Görme)
        print(f"{Fore.CYAN}[14/15] Continuous Vision...{Style.RESET_ALL}")
        try:
            from vision.continuous_vision import get_continuous_vision
            self._continuous_vision = get_continuous_vision()
            # Servo callback bağla
            if self._smooth_motion:
                self._continuous_vision.servo_callback = lambda p, t: self._smooth_motion.move_smooth(pan=p, tilt=t, duration_ms=100)
            self._continuous_vision.start()
            print(f"{Fore.GREEN}    └── Sürekli görme aktif{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}    └── Hata: {e}{Style.RESET_ALL}")
        
        # 15. Stereo Coordination (100mm Stereo)
        print(f"{Fore.CYAN}[15/15] Stereo Coordination...{Style.RESET_ALL}")
        try:
            from vision.stereo_coordination import get_stereo_coordination
            self._stereo_coordination = get_stereo_coordination(baseline_mm=100)
            print(f"{Fore.GREEN}    └── 100mm stereo koordinasyon aktif{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}    └── Hata: {e}{Style.RESET_ALL}")
        
        # Robotik modüller (opsiyonel - servo olmadan simülasyon)
        try:
            from robotics.eye_contact import get_eye_contact
            from robotics.conversational_gestures import get_conversational_gestures
            self._eye_contact = get_eye_contact()
            self._conversational_gestures = get_conversational_gestures()
            # SmoothMotion bağla
            if self._smooth_motion:
                self._eye_contact.smooth_motion = self._smooth_motion
                self._conversational_gestures.smooth_motion = self._smooth_motion
            print(f"{Fore.GREEN}    └── Göz teması ve jestler aktif{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}    └── Robotik: {e}{Style.RESET_ALL}")
        
        print(f"""
{Fore.GREEN}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     ✓ DERİN v10.2 ONLINE                                     ║
║     İsim: {identity.name:<20}                              ║
║     Ses: {identity.voice.voice_id:<25}                  ║
║                                                               ║
║     🧠 Beyin Entegrasyonu: Aktif                             ║
║     👁️ Sürekli Görme: Aktif                                   ║
║     🤖 Akıcı Hareket: Aktif                                   ║
║                                                               ║
║     Model yükleme başlıyor...                                ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
""")
        
        # ═══════════════════════════════════════════════════════════════
        # AŞAMALI MODEL YÜKLEME (Thor için optimize)
        # Modeller sırayla yüklenir - memory spike önlenir
        # ═══════════════════════════════════════════════════════════════
        self._load_models_staged()
        
        print(f"{Fore.GREEN}[CNS] Konuşmaya başla, dinliyorum... (Ctrl+C ile çık){Style.RESET_ALL}")
        
        self._running = True
    
    def run(self):
        """Ana döngü"""
        try:
            while self._running:
                # Hypothalamus durumunu Limbic'e aktar
                if self._hypothalamus and self._limbic:
                    state = self._hypothalamus.state
                    self._limbic.update_from_hypothalamus(
                        state.energy,
                        state.is_sleeping or state.energy < 30
                    )
                
                # Sıcaklık kontrolü - Occipital FPS ayarla
                if self._hypothalamus and self._occipital:
                    fps = self._hypothalamus.get_vision_fps()
                    self._occipital.set_fps(fps)
                
                # v10.1: Meta-cognition güncelle
                if self._meta_cognition:
                    try:
                        self._meta_cognition.update_cognitive_load()
                    except:
                        pass
                
                # v10.2: Smooth motion idle animasyonu
                if self._smooth_motion and not self._smooth_motion.is_moving():
                    # Canlılık sistemi zaten çalışıyor (nefes, jitter)
                    pass
                
                time.sleep(5.0)
                
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[CNS] Kapatılıyor...{Style.RESET_ALL}")
            self.shutdown()
    
    def shutdown(self):
        """Sistemi kapat"""
        self._running = False
        
        # Event bus'ı durdur
        if self._event_bus:
            self._event_bus.stop()
        
        # Thread'leri durdur
        for t in self._threads:
            if hasattr(t, 'stop'):
                t.stop()
        
        # Bekle
        for t in self._threads:
            if t.is_alive():
                t.join(timeout=2.0)
        
        print(f"{Fore.GREEN}[CNS] Hoşçakal!{Style.RESET_ALL}")


def main():
    """Ana giriş noktası"""
    cns = DerinCNS()
    
    # SIGINT handler
    def signal_handler(sig, frame):
        cns.shutdown()
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    
    # Boot ve çalıştır
    cns.boot()
    cns.run()


if __name__ == "__main__":
    main()
