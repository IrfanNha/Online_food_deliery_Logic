#include<iostream>
	
using namespace std;

int main(){
	
	//Deklarasi Variabel
	int pil;
	float harga, jarak;
	
	cout << "================================\n" << endl;
	cout << "SELAMAT DATANG DI X FOOD XPRESS \n" << endl;
	cout << "================================\n" << endl;
	
	cout << "================================\n" << endl;
	cout << "===============Menu=============\n" << endl;
	cout << "1. Nasi goreng : 10.000           " << endl;
	cout << "2. Bakmi       : 12.000           " << endl;
	cout << "================================\n" << endl;
	cout << "Masukkan Pilihan menu anda (Nomor) = "; cin >> pil;
	//Pemesanan Nasgor
	if(pil ==1){
		cout << "Pesanan Anda adalah NASI GORENG " << endl;
		
		cout << "Masukkan Jarak anda yang ada di MAPS =" ; cin >> jarak;
		if(jarak <=0){
			cout << "Angka Tidak Valid " << endl;
		}else{
			cout << "Masukkan Jarak anda yang ada di MAPS =" ; cin >> jarak;
			if(jarak <=11){
				cout <<"totalnya =" << 10000 + (jarak * 800) + (10000 * 5/100) << endl;
			}
			else if(jarak <=21){
				cout <<"totalnya =" << 10000 + (jarak * 800) + (10000 * 6/100) << endl;
			}
			else if(jarak <=31){
				cout <<"totalnya =" << 10000 + (jarak * 800) + (10000 * 7/100) << endl;
			}
			else if(jarak >=31){
				cout <<"Maaf Jarak Anda Terlalu Jauh" << endl;
			}
		}
		
	}
		//Pemesanan Bakmi
	if(pil ==2){
		cout << "Pesanan Anda Anda adalah BAKMI " << endl;
		
		cout << "Masukkan Jarak anda yang ada di MAPS =" ; cin >> jarak;
		if(jarak <=0){
			cout << "Angka Tidak Valid " << endl;
		}else{
			cout << "Masukkan Jarak anda yang ada di MAPS =" ; cin >> jarak;
			if(jarak <=11){
				cout <<"totalnya =" << 12000 + (jarak * 800) + (12000 * 5/100) << endl;
			}
			else if(jarak <=21){
				cout <<"totalnya =" << 12000 + (jarak * 800) + (12000 * 6/100) << endl;
			}
			else if(jarak <=31){
				cout <<"totalnya =" << 12000 + (jarak * 800) + (12000 * 7/100) << endl;
			}
			else if(jarak >=31){
				cout <<"Maaf Jarak Anda Terlalu Jauh" << endl;
			}
		}
		
	}
	cout << "Terima Kasih Sudah Berbelanja di X FOOD XPRESS" <<endl;
	
	return 0;	
}
