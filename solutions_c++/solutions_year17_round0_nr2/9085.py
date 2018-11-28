#include <bits/stdc++.h>
using namespace std;

int main(int arc,char * argv[]){

	freopen("B-small-attempt0.in", "r", stdin);
  freopen("B-small-attempt0.out", "w", stdout);
	int  t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{    ios::sync_with_stdio(false);
         cin.tie(NULL);
		long long s;
		cin >> s;
		long long temp = s;
		int k  = -1;
		while (temp)
		{	temp = temp/10;
			k++;
		}
		temp = 10;
		for (int j = 0; j < k; ++j)
		{ 
			while ( ((s% temp ) /(temp/10))  < (( s % (temp*10))/temp) )
				s--;
			temp*=10;
		}
		
		
		
		
		cout << "Case #" << (i+1) << ": " <<s << endl;
	}
}