"""
ad soyad = 
numara = 
"""


class Hesap: 
    """Hesap ve harcama bilgilerini tutan sınıf"""

    def __init__(self,ad,soyad,baslangic_bakiyesi) -> None:
        """Hesap Constructor

        Args:
            ad (str): kişi adı
            soyad (str): kişi soyadı
            baslangic_bakiyesi (str): hesap açılış bakiyesi
        """ 

 
    def ad(self):
        """ad property getter

        Returns:
            str: adın ilk üç harfi ve 3 yıldız
            örnek: Ayş***
        """ 
 
    def ad(self,value):
        """ad setter

        Args:
            value (str): kişi adı
        """ 
 
    def soyad(self):
        """soyad setter

        Returns:
            str: soyadın ilk üç harfi ve 3 yıldız
            örnek: Yıl***
        """ 
 
    def soyad(self,value):
        """soyad setter

        Args:
            value (str): kişi soyadı
        """ 
 
    def bakiye(self):
        """bakiye property

        Returns:
            float: kişi bakiyesi
        """ 
 
    def bakiye(self,value):
        """bakiye setter

        Args:
            value (float): bakiye property si read-only dir

        Raises:
            AttributeError: Bakiye değiştirilemez!
        """ 

    def __hareket_ekle(self,aciklama,miktar):
        """hareket ekle methodu

        Args:
            aciklama (str): hareket açıklaması
            miktar (float): miktar 
        """ 

    def yatir(self,value):
        """para yatirma methodu

        Args:
            value (float): yatan miktar
        miktar negatif olursa aşağıdaki hata gerçekleşmelidir.

        Raises:
            AttributeError: Yatırılan miktar 0'dan büyük olmalıdır!
        """ 

    def harca(self,aciklama,miktar):
        """harcama methodu

        Args:
            aciklama (str): harcama açıklaması
            miktar (float): miktar

            miktar negatif olursa aşağıdaki hata gerçekleşir
        Raises:
            AttributeError: Harcanan miktar 0'dan büyük olmalıdır!
        
            miktar bakiyeden büyük olursa aşağıdaki hata gerçekleşir
        Raises:
            AttributeError: Bakiye yetersiz!
        """ 

    def dokum(self):
        """hesap dokumu methodu 
        önce ------ yazar 20 çizgi
        sonra kişinin adı ve soyadı yazar
        sonra tüm hareketler alt alta yazılır
        sonra hesap bakiyesi yazılır
        sonra ------ yazar 20 çizgi
        
        """ 
