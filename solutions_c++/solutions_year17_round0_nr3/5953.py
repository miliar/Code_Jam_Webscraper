#include<bits/stdc++.h>
using namespace std;
#define f(i, a, b) for(int i=a; i<=b; i++)

int maximo(int a, int b)
{
	if(a>b)
		return a;
	return b;
}
int minimo(int a, int b)
{
	if(a<b)
		return a;
	return b;
}

int main()
{
	int T;
	cin>>T;

	list<int> v;
	f(t, 1, T)
	{
		v.clear();
		int n, k;
		cin>>n>>k;
		v.push_back(n);

		list<int>::iterator pos_maior;
		for(int j=1; j<=k;j++){
			int maior = *(v.begin());
			pos_maior = v.begin();
			for(auto it = v.begin(); it !=v.end(); it++)
			{
				if(*it > maior) // ESTRITO
				{
					maior = *it;
					pos_maior = it;
				}
			}

			v.insert(pos_maior, (maior-1)/2);
			*pos_maior = (maior-1)-(maior-1)/2;
		}
		list<int>::iterator p = pos_maior; pos_maior--;
		cout<<"Case #"<<t<<": "<<maximo(*p, *pos_maior)<<" "<<minimo(*p, *pos_maior)<<endl;

	}

	return 0;
}