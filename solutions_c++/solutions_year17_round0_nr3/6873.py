#include <iostream>
#include <stdio.h>
#include <algorithm> 
#include <vector>



using namespace std;

typedef vector<int> vi;
vi number;

int main()
{
	int t,espacios,personas;
	scanf("%d",&t);
	int aux,min,max;
	
	for (int i = 1; i <= t; ++i)
	{
		scanf("%d %d",&espacios,&personas);
		if(espacios==personas){printf("Case #%d: %d %d\n",i,0,0 );}else
		if(personas==1 ){ if(espacios%2==0){ printf("Case #%d: %d %d\n",i,espacios/2,(espacios/2)-1 ); }else{printf("Case #%d: %d %d\n",i,espacios/2,espacios/2 );} }
		else{
			for (int j = 1; j <=personas ; ++j)
			{
				
				if(j==1){aux=espacios;}else{
					sort(number.begin(),number.end());
					aux=number[number.size()-1];
					number.erase(number.begin()+(number.size()-1));
				}
				if(aux%2==0){min=(aux/2)-1; max=aux/2;}else{
					min=aux/2;
					max=aux/2;
				}
				number.push_back(min);
				number.push_back(max);

			}
			printf("Case #%d: %d %d\n",i,max,min);

		}
		

		number.clear();
	}
	return 0;
}