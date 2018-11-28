#include <iostream>
#include <vector>
#include <iomanip>
#include <set>
#include <cmath>

using namespace std ;


void solve()
{
	set< pair< pair<int, int>, int >, greater< pair<pair<int, int>, int> > > Q ;
	set< pair< pair<int, int>, int > >::iterator it ;
	vector<int> v ;
	int N, R, O, Y, G, B, V ;

	cin >> N >> R >> O >> Y >> G >> B >> V ;

	if(R >= Y && R >= B)
	{
		if(R != 0)
			Q.insert(make_pair(make_pair(R, true), 0)) ;
		if(Y != 0)
			Q.insert(make_pair(make_pair(Y, false), 1)) ;
		if(B != 0)
			Q.insert(make_pair(make_pair(B, false), 2)) ;
	}
	else if(Y >= R && Y >= B)
	{		
		if(R != 0)
			Q.insert(make_pair(make_pair(R, false), 0));
		if(Y != 0)
			Q.insert(make_pair(make_pair(Y, true), 1)) ;
		if(B != 0)
			Q.insert(make_pair(make_pair(B, false), 2)) ;
	}
	else if(B >= R && B >= Y)
	{
		if(R != 0)
			Q.insert(make_pair(make_pair(R, false), 0)) ;
		if(Y != 0)
			Q.insert(make_pair(make_pair(Y, true), 1)) ;
		if(B != 0)
			Q.insert(make_pair(make_pair(B, false), 2)) ;
	}

	int freq, priority, type ;
	int prev = -1 ;

	while(!Q.empty())
	{
		it = Q.begin() ;

		if(Q.begin()->second == prev)
		{
			++it ;
			if(it == Q.end())
				--it ;
		}

		freq = it->first.first ;
		priority = it->first.second ;
		type = it->second ;

		Q.erase(it) ;

		v.push_back(type) ;
		freq-- ;

		if(freq != 0)
			Q.insert(make_pair(make_pair(freq, priority), type)) ;

		prev = type ;
	}

	bool ok = true ;
	for(int i = 0 ; i < N-1 ; i++)
		if(v[i] == v[i+1])
			ok = false ;

	if(v[0] == v[N-1])
		ok = false ;

	if(!ok)
		cout << "IMPOSSIBLE" ;
	else
	{
		for(int i = 0 ; i < N ; i++)
		{
			if(v[i] == 0)
				cout << 'R' ;
			else if(v[i] == 1)
				cout << 'Y' ;
			else
				cout << 'B' ;
		}
	}
}

int main()
{
    ios::sync_with_stdio(false) ;
    cin.tie(0) ;
    
    int T ;
    cin >> T ;
    
    for(int i = 1 ; i <= T ; i++)
    {
        cout << "Case #" << i << ": " ;
        solve() ;
        cout << "\n" ;
    }
    
    
    return 0 ;
}