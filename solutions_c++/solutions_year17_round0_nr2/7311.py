#include <iostream>

using namespace std;

void reverse(int a[], int l, int r) 
{
	for(int i=l,j=r; i < j; ++i, --j) 
	{
		int tmp = a[i];
		a[i] = a[j];
		a[j] = tmp;
	}
}

typedef long long ll;

int main() 
{
	int t, a[50];
	ll n;

	cin >> t;

	for(int tc = 1; tc <= t; ++tc) 
	{
		cin >> n;

		cout << "Case #" << i << ": ";
		if(n < 10)  // single digit number
		{
			cout << n << "\n";
			continue;
		}

		int cnt = 0;
		
		// store it in an array
		for(ll dupN = n; dupN > 0 ; dupN /= 10)
			a[cnt++] = dupN%10;

		// reverse
		reverse(a, 0, cnt-1);

		int idx, i;
		for(i=0; i<cnt-1; ++i) 
		{
			if(a[i] > a[i+1])
			{
				// store the index
				a[i]--;
				idx = i+1;
				break;
			}		
		}

		if(i == cnt-1) 
		{
			cout << n << "\n";
			continue;
		}

		// see if the change made impact the previous digit
		for(int j=i; j>0; --j)
		{
			if(a[j-1] > a[j])
			{
				a[j-1]--;
				idx = j;
			}
		}

		// fill all 9s from idx to cnt
		for(int j=idx; j<cnt; ++j)
			a[j] = 9;

		// remove all previous 9
		for(int j=0; j<cnt; ++j)
		{
			if(a[j] != 0)
				cout << a[j];
		}

		cout <<"\n";
	}

	return 0;
}