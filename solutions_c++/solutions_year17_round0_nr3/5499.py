#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <algorithm>

using namespace std;

long long CalculateLs(long long a, vector<long long>&);
long long CalculateRs(long long a, long long b, vector<long long>&);
long long CalculateLsFaster(long long qualePosto, long long da, long long a);
long long CalculateRsFaster(long long qualePosto, long long da, long long a);
long long FindBestStall(long long a, vector<long long>&, bool b);

unsigned long int MinLsRs, MaxLsRs;

int main(){
	  ifstream in("input.txt");
  	ofstream out("output.txt");
  
  	long long nRighe;
  	in >> nRighe;

  	for(long long i = 0; i < nRighe; i++)
  	{
  		//cout << "----------" << endl;

  		long long posti;
      long long nPersone;
      vector<long long> indiciOccupati;

  		in >> posti >> nPersone;

      indiciOccupati.resize(2);
      indiciOccupati[0] = -1;
      indiciOccupati[1] = posti;



  		/**/

  		//Le persone si posizionano
  		for(long long j = 0; j < nPersone; j++)
  		{
  			long long best;
  			if(j == nPersone - 1)
  				best = FindBestStall(posti, indiciOccupati, true);
  			else
  				best = FindBestStall(posti, indiciOccupati, false);
  			indiciOccupati.push_back(best);

  			sort(indiciOccupati.begin(), indiciOccupati.end());
  			//cout << best << endl;
  		}

  		out << "Case #" << i+1 << ": " << MaxLsRs << " " << MinLsRs << endl;
  	}
  
  	return 0;
}

long long CalculateLs(long long qualePosto, vector<long long> &occupati)
{
	long long minAttuale = qualePosto;

	for(long long i = 0; i < occupati.size(); i++)
	{
		if(occupati[i] == qualePosto)
			return 0;
		if(occupati[i] < qualePosto && (qualePosto - occupati[i] - 1) < minAttuale )
			minAttuale = qualePosto - occupati[i] - 1;
	}

	return minAttuale;
}

long long CalculateRs(long long qualePosto, long long posti, vector<long long> &occupati)
{
	long long minAttuale = posti - qualePosto - 1;

	for(long long i = 0; i < occupati.size(); i++)
	{
		if(occupati[i] == qualePosto)
			return 0;
		if(occupati[i] > qualePosto && (occupati[i] - qualePosto - 1) < minAttuale )
			minAttuale = occupati[i] - qualePosto - 1;
	}

	return minAttuale;
}

long long CalculateLsFaster(long long qualePosto, long long da, long long a)
{
	return qualePosto - da;
}

long long CalculateRsFaster(long long qualePosto, long long da, long long a)
{
	return a - qualePosto - 1;
}

long long FindBestStall(long long quantiPosti, vector<long long> &occupati, bool isLast)
{
	vector<long long> postiMigliori;
	long long valoreMigliore = 0;

	//cerco lo spazio piu grande
	int spazioMax = 0;
	int da = 0, a = quantiPosti; //da incluso, a escluso
	if(occupati.size() > 0)
	{
		

		for(int i = 0; i < occupati.size() - 1; i++)
		{
			if(occupati[i+1] - occupati[i] - 1 > spazioMax)
			{
				spazioMax = occupati[i+1] - occupati[i] - 1;
				da = occupati[i] + 1;
				a = occupati[i+1];
			}
		}

	}

	//cout << "Spazio Max: " << spazioMax << endl;

	//cerco il posto migliore
	for(long long i = da; i < a; i++)
	{
		//long long tmp = min(CalculateLs(i, occupati), CalculateRs(i, quantiPosti, occupati));
		long long tmp = min(CalculateLsFaster(i, da, a), CalculateRsFaster(i, da, a));
		if(tmp > valoreMigliore)
		{
			postiMigliori.clear();
			postiMigliori.push_back(i);
			valoreMigliore = tmp;
		}
		else if(tmp == valoreMigliore)
			postiMigliori.push_back(i);
	}

	//Tra questi cerco quello con max(Ls, Rs) migliore
	vector<long long> postiAncoraMigliori;
	long long valoreAncoraMigliore = 0;

	for(long long i = 0; i < postiMigliori.size(); i++)
	{
		//long long tmp = max(CalculateLs(i, occupati), CalculateRs(i, quantiPosti, occupati));
		long long tmp = max(CalculateLsFaster(i, da, a), CalculateRsFaster(i, da, a));
		if(tmp > valoreAncoraMigliore)
		{
			postiAncoraMigliori.clear();
			postiAncoraMigliori.push_back(postiMigliori[i]);
			valoreAncoraMigliore = tmp;
		}
		else if(tmp == valoreAncoraMigliore)
			postiAncoraMigliori.push_back(postiMigliori[i]);
	}

	//Cerco quello piu a sinistra di questi
	long long tmp = postiAncoraMigliori[0];
	for(long long i = 0; i < postiAncoraMigliori.size(); i++)
		if(postiAncoraMigliori[i] < tmp)
			tmp = postiAncoraMigliori[i];

	//debug
		/*
	cout << "occupati: " << endl;
	for(int i = 0; i < occupati.size(); i++)
		cout << occupati[i] << endl;
	cout << CalculateLs(tmp, occupati) << ";" << CalculateRs(tmp, quantiPosti, occupati) << endl;
	cout << tmp << endl;
	*/

	if(isLast)
	{
		//MaxLsRs = max( CalculateLs(tmp, occupati), CalculateRs(tmp, quantiPosti, occupati));
		//MinLsRs = min( CalculateLs(tmp, occupati), CalculateRs(tmp, quantiPosti, occupati));
		MaxLsRs = max( CalculateLsFaster(tmp, da, a), CalculateRsFaster(tmp, da, a));
		MinLsRs = min( CalculateLsFaster(tmp, da, a), CalculateRsFaster(tmp, da, a));
	}

	return tmp;

}