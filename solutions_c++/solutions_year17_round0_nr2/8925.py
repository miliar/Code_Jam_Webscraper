#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

#define REP(i,b) for(int i=0; i<b; ++i);
typedef vector<int> vi;
vi number;

bool descomposicion(int n){
	int u,d,c,aux;
	u=n%10;

	aux=n;
	aux=aux%100;
	d=aux/10;
	if(d<=u){
		aux=n-d*10-u;
		c=aux/100;
		if(c<=d){return true;}else{return false;}
	}else{ return false;}
	
}
int main()
{
	int t,n;
	bool flag=false;
	scanf("%d",&t);
	for (int i = 1; i <= t; ++i)
	{
		scanf("%d",&n);
		for (int j = n; j > 0 ; --j)
		{
			flag= descomposicion(j);
			if(flag){
				printf("Case #%d: %d\n",i,j );
				break;
			}else{
				flag=true;
			}
		}

	}
	
	return 0;
}