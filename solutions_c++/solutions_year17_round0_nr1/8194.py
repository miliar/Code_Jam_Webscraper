#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ofstream fout("output.txt");
ifstream fin("input.txt");

inline void increment(ll &n){

	if(n==INT_MAX) n=1;

	else ++n;

}

int main(){

	ll t,k,i,j,counter=0;

	fin>>t;

	while(t--){

		string s,cp1,cp2;

		fin>>s>>k;

		cp1=s;

		cp2=s;

		ll f1=INT_MAX,f2=INT_MAX;

		for(i=0;i<s.size()-k+1;++i){

			if(cp1[i]=='-'){

				increment(f1);

				for(j=i;j<i+k;++j){

					if(cp1[j]=='-') cp1[j]='+';

					else cp1[j]='-';

				}

				//fout<<i<<"--->"<<cp1<<"  "<<f1<<"\n";


			}


		}

		for(i=s.size()-1;i>=k-1;--i){

			if(cp2[i]=='-'){

				increment(f2);

				for(j=i;j>i-k;--j){

					if(cp2[j]=='-') cp2[j]='+';

					else cp2[j]='-';

				}


			}

		//	fout<<i<<"--->"<<cp2<<"  "<<f2<<"\n";


		}

		if(f1==INT_MAX) f1=0;
		if(f2==INT_MAX) f2=0;


		fout<<"Case #"<<++counter<<": ";

		bool flag1=(find(cp1.begin(),cp1.end(),'-')!=cp1.end());//found in 1

		bool flag2=(find(cp2.begin(),cp2.end(),'-')!=cp2.end());//found in 2

		if(flag1 && flag2) fout<<"IMPOSSIBLE";

		else{

			if(!flag1 && !flag2) fout<<min(f1,f2);
			else if(!flag1) fout<<f1;
			else fout<<f2;

		}

		fout<<"\n";




	}

}