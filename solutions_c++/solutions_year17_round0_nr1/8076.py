#include <bits/stdc++.h>
using namespace std;

#define vi vector<int>
#define pb push_back
#define ll unsigned long long int

int move(vi pan, int k)
{
	int move = 0;
	//cout << "k: " << k << endl;
	
	//for(int j=0; j<(int)pan.size(); j++) cout << pan[j] << " ";
	//cout << endl;
	
	for(int i=0; i<(int)pan.size()-k+1; i++)
	{
		//cout << "i: " << i << "pan[i] = " << pan[i] << endl;
		if(pan[i] == 0)
		{
			//cout << "Here" << endl;
			
			for(int j=0; j<k; j++)
			{ 
				if(pan[i+j] == 0) pan[i+j] = 1;
				else pan[i+j] = 0;
			}
			
			move++;
			//for(int j=0; j<(int)pan.size(); j++) cout << pan[j] << " ";
			//cout << endl;
		}
	}
	
	for(int i=0; i<(int)pan.size(); i++)
		if(pan[i] == 0) return -1;
	
	return move;
}

int main()
{
	int testes, k;
	
	
	cin >> testes;
	for(int i=1; i<=testes; i++)
	{	
	    vi pan;
	    string heyo;
	    cin >> heyo;
		for(int ind=0; ind < heyo.length(); ind++)
		{
			//cout << "now: " << now << endl;
			if(heyo[ind] == '+') pan.pb(1);
			else if(heyo[ind] == '-') pan.pb(0);
		}
		
		//for(int j=0; j<(int)pan.size(); j++) cout << pan[j] << " ";
		//cout << endl;
		cin >> k;
		//cout << "k: " << k << endl;
		int m = move(pan, k);
		
		if(m == -1) cout << "Case #" << i << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << i << ": " << move(pan, k) << endl;		
	}

	return 0;
}
