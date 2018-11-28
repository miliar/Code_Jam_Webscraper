#include <bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;

int main() {
	// your code goes here
	int t, i;
	cin >> t;
	for(i = 1; i <= t; i++)
	{
	    string n;
	    int nod, rep = 1, j;
	    cin >> n;
	    nod = n.length();
	    for(j = 0; j < nod-1; j++)
	    {
	        if((n[j] - '0') == (n[j+1] - '0'))
	        {
	            rep++;
	        }
	        else if((n[j] - '0') > (n[j+1] - '0'))
	        {
	            int idx = j+1;
	            while(rep--)
	                n[idx--] = '9';
	            
                if((n[j+1] - '0') == 0)
	                n[idx] = '9';
	            else
	                n[idx] = --n[idx];
	            
                break;
	        }
	        else
	            rep = 1;
	    }
	    cout << "Case #" << i << ": ";
	    for(((n[0]-'0') == 0)?(j = 1):(j = 0); j < nod && (n[j] - '0') != 9; j++)
	        cout << n[j];
	    for(int k = j; k < nod; k++)
	        cout << 9;
	    cout << '\n';
	}
	return 0;
}
