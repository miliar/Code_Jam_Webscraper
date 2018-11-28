#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef long long ll;


ll b, d;
ll dragonHealth;

ll fewest;
std::unordered_map<string,ll> mymap;

struct unitIt
{
	ll hD;
	ll aD;
	ll hK;
	ll aK;
	ll move;
};

std::queue<unitIt> myqueue;

ll queueIt(ll hD1, ll aD1, ll hK1, ll aK1, ll move1)
{
	unitIt newUnit;
	newUnit.hD = hD1;
	newUnit.aD = aD1;
	newUnit.hK = hK1;
	newUnit.aK = aK1;
	newUnit.move = move1;
	myqueue.push(newUnit);
	
	
	while(myqueue.size() > 0)
	{
		
		unitIt temp = myqueue.front();
		myqueue.pop();
		string key = to_string(temp.hD) + " " + to_string(temp.aD) + " " + to_string(temp.hK) + " " + to_string(temp.aK) + " " + to_string(temp.move % 2);
		//cout << "Key " << key << endl;
		if(mymap.find(key) != mymap.end())
		{
			//cout << "Found " << hD << " " << aD << " " << hK << " " << aK << " " << move << endl;
				continue;
		}
		mymap[key] = temp.move;
		if(temp.hD <= 0)
		{
			//cout << "Ran1" << endl;
			continue;
		}
		
		if(temp.hK <= 0)
		{
			//cout << "Ran2" << endl;
			//cout << key << endl;
			if(temp.move < fewest)
			{
				fewest = temp.move;
			}
			return 0;
		}
		
		
		if(temp.move % 2 == 1)
		{
			//cout << "Here" << endl;
			newUnit.hD = temp.hD - temp.aK;
			newUnit.aD = temp.aD;
			newUnit.hK = temp.hK;
			newUnit.aK = temp.aK;
			newUnit.move = temp.move + 1;
			myqueue.push(newUnit);
			continue;
		}
		
		
		newUnit.hD = temp.hD;
		newUnit.aD = temp.aD;
		newUnit.hK = temp.hK - temp.aD;
		newUnit.aK = temp.aK;
		newUnit.move = temp.move + 1;
		myqueue.push(newUnit);
		
		newUnit.hD = temp.hD;
		newUnit.aD = temp.aD + b;
		newUnit.hK = temp.hK;
		newUnit.aK = temp.aK;
		newUnit.move = temp.move + 1;
		myqueue.push(newUnit);
		
		newUnit.hD = temp.hD;
		newUnit.aD = temp.aD;
		newUnit.hK = temp.hK;
		newUnit.aK = max(temp.aK - d, (ll)0);
		newUnit.move = temp.move + 1;
		myqueue.push(newUnit);
		
		newUnit.hD = dragonHealth;
		newUnit.aD = temp.aD;
		newUnit.hK = temp.hK;
		newUnit.aK = temp.aK;
		newUnit.move = temp.move + 1;
		myqueue.push(newUnit);

	}

}

ll recurseIt(ll hD, ll aD, ll hK, ll aK, ll move)
{
	//cout << "Move " << hD << " " << aD << " " << hK << " " << aK << " " << move << endl;
	
	string key = to_string(hD) + " " + to_string(aD) + " " + to_string(hK) + " " + to_string(aK) + " " + to_string(move%2);
	if(mymap.find(key) != mymap.end())
	{
		//cout << "Found " << hD << " " << aD << " " << hK << " " << aK << " " << move << endl;
		if(mymap[key] < move)
			return 0;
	}
	mymap[key] = move;
	
	
	
	if(hD <= 0)
	{
		//cout << "Ran1" << endl;
		return 0;
	}
	if(hK <= 0)
	{
		//cout << "Ran2" << endl;
		if(move < fewest)
		{
			fewest = move;
		}
		return 0;
	}
	
	if(move > fewest || move > 25)
	{
		return 0;
	}
	
	if(move % 2 == 1)
	{
		return recurseIt(hD - aK, aD, hK, aK, move + 1);
	}
	recurseIt(hD, aD, hK - aD, aK, move + 1);
	recurseIt(hD, aD + b, hK, aK, move + 1);
	recurseIt(dragonHealth, aD, hK, aK, move + 1);
	recurseIt(hD, aD, hK, max(aK - d, (ll)0), move + 1);
	return 0;
}


int main()
{
	ll casses;
	cin >> casses;
	
	
	
	for(int caseNum = 1; caseNum <= casses; caseNum++)
	{
		ll hD, aD, hK, aK;
		cin >> hD >> aD >> hK >> aK >> b >> d;
		dragonHealth = hD;
		fewest = 999999;
		queueIt(hD, aD, hK, aK, 0);
		if(fewest > 10000)
		{
			cout << "Case #" << caseNum << ": IMPOSSIBLE" << endl;
		}else
		{
			cout << "Case #" << caseNum << ": " << ceil(fewest/2.0) << endl;
		}
		std::queue<unitIt> empty;
   	std::swap( myqueue, empty );
   	mymap.clear();

		
	}
	return 0;
}










