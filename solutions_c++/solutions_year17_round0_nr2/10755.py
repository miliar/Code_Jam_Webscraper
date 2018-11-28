#include<bits/stdc++.h>
using namespace std;

int main(){

  int T;
  cin>>T;

  for (int i = 0; i < T; ++i)
  {
	  	long long int N;
	  	cin>>N;
	  	vector <int> a(18,0);

	  	while(N>=0){
		  	long long K = N;
		  	int l = 17,f=0;
		  	while(K>=1){
		  		int r = K%10;
		  		a[l--] = r;
		  		K = K/10;
		  	}
		  	for (int j = 17; j>0; j--)
		  	{
		  		if(a[j]<a[j-1]){
		  			N--;
		  			l=17;
		  			f=1;
		  			break;
		  		}
		  	}
		  	if(f==0){
		  		cout<<"Case #"<<i+1<<": "<<N<<endl;
		  		break;
		  	}
    }
  }
}