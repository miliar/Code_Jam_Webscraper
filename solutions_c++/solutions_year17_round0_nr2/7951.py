#include<bits/stdc++.h>

using namespace std;

int main()
{ int t;
	cin >> t;
	for( int i=0;i<t;i++)
	{
		string s;
		cin >> s;
		int sl = s.length();
		if( sl == 1 )
		{  cout << "Case #" << i+1 << ':'<<' '; 
			cout << s << endl;
			continue;	}
		int  a[s.length()];
		for(int j=0;j< sl ;j++ )
		{

			a[j] = s[j] - '0';
		}

		int k = 0;
		while(k < sl -1 && a[k] <= a[k+1]  )
		{k++;}
		if( k != sl -1 )
		{	
			for(int h=k+1 ; h<sl ; h++  )
			{ a[h]=9; }
			a[k]-=1;
			while( k>0 && a[k-1] > a[k])
			{
				a[k] =9;
				a[k-1] -=1;
				k--;
			}
		}
 cout << "Case #" << i+1 << ':'<<' '; 
                if( a[0] != 0)
			cout << a[0];
		for(int y=1;y<s.length();y++)
		{ 
			cout << a[y];}
		cout << endl;

	}

	return 0;

} 

