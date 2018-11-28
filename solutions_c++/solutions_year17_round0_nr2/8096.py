#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long int

ll soma[20];

int dig(ll n)
{
	int digitos = 0;
	while(n > 0)
	{
		n = n/10;
		digitos++;
	}
	
	return digitos;
}

ll pot(ll base, int exp)
{
	if(exp == 0) return 1;

	ll result = 1;
	for(int i=1; i<=exp; i++) result *= base;
	
	return result;
}

ll numerize(int n[20], int dig)
{
	ll result = 0, now = 1;
	for(int i=dig; i>=1; i--)
	{
		result += n[i]*now;
		now = now*10;
	}
	
	return result;
}

ll last(int n[20], int dig)
{
	if(dig == 1) return numerize(n, dig);

	for(int i=dig; i>=2; i--)
	{
		if(n[i] < n[i-1])
		{
			n[i-1]--;
			for(int j=i; j<=dig;j++) n[j] = 9;
		}
	}
	
	int copy[20];
	memset(copy, 0, sizeof copy);
	
	int k=1;
	while(n[k] == 0) k++;
	
	for(int i=k; i<=dig; i++) copy[i-k+1] = n[i];
	
	return numerize(copy, dig-k+1);
}

int main()
{
	ll casos;
	int v[20];
	cin >> casos;
	
	for(int i=1; i<=casos; i++)
	{
		ll x, aux;
		cin >> x;
			aux = x;
		int d = dig(x)-1;
		memset(v, 0, sizeof v);
		for(int j=d+1; j>=1; j--)
		{
			//cout << "j: " << j << endl;
			v[j] = aux%10;
			aux = aux/10;
		}
		
		//for(int k=1; k<=d+1; k++) cout << v[k] << " ";
		
		cout << "Case #" << i << ": " << last(v, d+1) << endl;
	}
}
