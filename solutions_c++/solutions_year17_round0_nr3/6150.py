

#include <iostream>
#include <math.h>
using namespace std;
int M(int k){ 
return max(0,max((k-1)/2,k-1-(k-1)/2));
}
long long int m(int k){
	return max(0,k-1-M(k));
}

int code(int k, int tab[20])	{

for (int i=0;i<20;i++){
	tab[i]=k%2;
	k=(k-tab[i])/2;	}
	return 0;
}

int indice(int k){
	return log(k)/log(2);
}


long long int solve(int tab[20],int N,int k){
	int res=N;
	if (k==1) return N;
	for (int i=0;i<indice(k);i++){
		if (tab[i]==0) res=M(res);
		else res=m(res);
		
	}
	
	return res;

}


int main()
{ int T;
long long int k,N, r;
  int tab[20];
 
 cin >> T;
 for (int i=0;i<T;i++){
 	cin >> N >> k; 
 	code(k,tab);
 	r=solve(tab,N, k);
	cout << "Case #"<<i+1<<": "<<M(r)<<" "<<m(r)<<endl;

 
}


  return 0 ;}
  
  
