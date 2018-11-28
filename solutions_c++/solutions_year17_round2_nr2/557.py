#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <sstream>
#include <stack>
#include <queue>
#include <map>
#include <climits>
#include <cstdio>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include <functional>
using namespace std;
#define db(a) (cout << (#a) << " = " << (a) << endl)
typedef long long ll;

bool foo(char a, char b)
{
	if(a=='R' && (b=='Y'||b=='B'||b=='G')) return true;
	if(a=='Y' && (b=='B'||b=='R'||b=='V')) return true;
	if(a=='B' && (b=='R'||b=='Y'||b=='O')) return true;
	if(a=='O' && b=='B') return true;
	if(a=='V' && b=='Y') return true;
	if(a=='G' && b=='R') return true;
	return false;
}

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		ll N,R,O,Y,G,B,V;
		cin>>N>>R>>O>>Y>>G>>B>>V;		
		if(R==G && (O|Y|B|V)==0)
		{
			string erg;
			for(ll i=0;i<R;i++) erg += "RG";
			cout << "Case #" << t+1 << ": " << erg << "\n";
			continue;
		}
		if(V==Y && (O|R|B|G)==0)
		{
			string erg;
			for(ll i=0;i<V;i++) erg += "VY";
			cout << "Case #" << t+1 << ": " << erg << "\n";
			continue;
		}
		if(O==B && (Y|R|V|G)==0)
		{
			string erg;
			for(ll i=0;i<O;i++) erg += "OB";
			cout << "Case #" << t+1 << ": " << erg << "\n";
			continue;
		}
		if((O>0 && B < O+1) || (G>0 && R < G+1) || (V>0 && Y < V+1))
		{
			cout << "Case #" << t+1 << ": IMPOSSIBLE\n";
			continue;
		}
		R -= G;
		B -= O;
		Y -= V;		
		if((R==0&&B==0) || (R==0&&Y==0) || (Y==0&&B==0))
		{
			cout << "Case #" << t+1 << ": IMPOSSIBLE\n";
			continue;
		}
		if(R > B+Y || B > R+Y || Y > R+B)
		{
			cout << "Case #" << t+1 << ": IMPOSSIBLE\n";
			continue;
		}
		string erg;
		while(R>0 || Y>0 || B>0)
		{
			char last;
			if(erg.size() > 0) last = erg[erg.size()-1];
			else last = 'X';
			bool bR,bY,bB;
			bR=bY=bB=false;
			if(last == 'R')
			{
				if(Y>=B) bY = true;
				else bB = true;
			}
			if(last == 'Y')
			{
				if(R>=B) bR = true;
				else bB = true;
			}
			if(last == 'B')
			{
				if(R>=Y) bR = true;
				else bY = true;
			}
			if(last == 'X') 
			{
				if(R>=Y && R>=B) bR = true;
				else if(Y>=B && Y>=R) bY = true;
				else bB = true;
			}
			
			if(bR)
			{
				if(G>0)
				{
					for(ll i=0;i<G;i++) erg += "RG";
					erg += "R";
					G=0;
				}
				else erg += "R";
				R--;
			}
			else if(bY)
			{
				if(V>0)
				{
					for(ll i=0;i<V;i++) erg += "YV";
					erg += "Y";
					V=0;
				}
				erg += "Y";
				Y--;
			}
			else if(bB)
			{
				if(O>0)
				{
					for(ll i=0;i<O;i++) erg += "BO";
					erg += "B";
					O=0;
				}
				erg += "B";
				B--;
			}
			else cout << "FUCK0\n";
		}
		if(erg[0] == erg[erg.size()-1]) swap(erg[erg.size()-1], erg[erg.size()-2]);
		
		
		if(erg.size() != N) cout << "FUCK1\n";
		for(size_t i=1;i<erg.size();i++)
		{
			if(!foo(erg[i-1], erg[i])) cout << "FUCK2\n";
		}
		if(!foo(erg[0], erg[erg.size()-1])) cout << "FUCK3\n";
		
		
		cout << "Case #" << t+1 << ": " << erg << "\n";
	}
  return 0;
}
