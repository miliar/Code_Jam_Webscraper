#include <iostream>
#include<string>
#include<fstream>
using namespace std;

bool comprobar(string S)
{
	for(int i=0;i<S.length();i++)
		if(S.at(i)=='-')
			return false;
	return true;
}



string analizar(string SOriginal, int K)
{
	string S=SOriginal;
	string rpta;
	if(comprobar(S)) 
	{
		rpta="0";
		return rpta;
	}	
	int contador=-1;
	for(int i=0;i<S.length()-K+1;i++)
	{
		if(S.at(i)=='-')
		{
			contador++;
			for(int j=0;j<K;j++)
			{
				if(S.at(i+j)=='+') S.at(i+j)='-';
				else S.at(i+j)='+';
			}
		}
	}
	if(!comprobar(S))
	{
		S=SOriginal;
		contador=-1;
		for(int i=S.length()-1;i>=K;i--)
		{
			if(S.at(i)=='-')
			{
				contador++;
				for(int j=0;j<K;j++)
				{
					if(S.at(i-j)=='+') S.at(i-j)='-';
					else S.at(i-j)='+';
				}
			}
		}
		if(comprobar(S))
		{
			contador++;
			rpta=to_string(contador);	
		}
		else
			rpta="IMPOSSIBLE";
		return rpta;

	}
	contador++;
	rpta=to_string(contador);
	return rpta;
}

void main() {
  //ofstream out("out.txt");
  //streambuf *coutbuf = cout.rdbuf();
  //cout.rdbuf(out.rdbuf());


  int T,K; cin >> T;
  string S;
  for(int i=1;i<=T;i++)
  {
	  cin>>S>>K;
	  if(S.length()>=2 && S.length()<=10)
		  cout << "Case #" << i << ": " << analizar(S,K) << endl;
  }
  system("pause");
}
