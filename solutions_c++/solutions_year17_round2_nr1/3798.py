#include<iostream>
#include<cstdio>
#include <iomanip> 
#include<string>
using namespace std;




int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);


	int T;
	cin >> T;



	


	for(int t = 1;t<=T;t++)
	{
		
		cout << "Case #" << t << ": "; 
			
		long int D;
		cin >> D;
		long long caballos;
		cin >> caballos;
		long float horasMax;
		bool definiMax = false;
		for(int r = 1;r<=caballos;r++)
		{
			long long posCaballo;
			long float velCaballo;
			cin >> posCaballo;
			cin >> velCaballo;
			if(r==1)
			{
				horasMax = (D-posCaballo)/velCaballo;
			}else{
				if((D-posCaballo)/velCaballo>horasMax)
				{
					horasMax = (D-posCaballo)/velCaballo;
				}
			}
		}

		 long float velocidadNecesaria = D/horasMax;

		cout <<  setprecision(14) << velocidadNecesaria << endl;
	
	}



	return 0;
}