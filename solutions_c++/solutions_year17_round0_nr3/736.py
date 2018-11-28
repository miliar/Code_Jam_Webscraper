#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;

typedef unsigned long long ll;

std::unordered_map<std::string,ll> mymap;
std::unordered_map<ll,ll> prune2Min;

ll n2, large;

ll recurse(ll n, ll k)
{
    string key = to_string(n) + "_" + to_string(k);
    if(mymap.find(key) != mymap.end())
    {
        return mymap[key];
    }
    
    
    if(prune2Min.find(n) != prune2Min.end())
    {
        if(prune2Min[n] > k)
        {
            cout << "Used " << endl;
            return 1000000000000000001;
        }
    }
    prune2Min[n] = k;
    //cout << n << " " << k << endl;
    
    
   
    if(k == 0)
    {
        string key = to_string(n) + "_" + to_string(k);
        mymap[key] = n;
        return n;
    }
    k = k - 1;
    
    if(n % 2 == 1)
    {
        if(k % 2 == 0)
        {
            //cout << "Two " << (n / 2) << " " << k/2 << endl;
            ll num = recurse((n / 2), k / 2);
            if(k == 0 && n <= n2)
            {
                //cout << "N k " << n << " " << k << endl;
                n2 = n;
                large = num;
            }
            string key = to_string(n) + "_" + to_string(k);
            mymap[key] = num;
            return num;
        }else if(k % 2 == 1)
        {
            //ll first = recurse((n / 2), k / 2);
            ll second = recurse((n / 2), k / 2 + 1);
            
            string key = to_string(n) + "_" + to_string(k);
            
            mymap[key] = second;
            return second;
            
            /*mymap[key] = std::min(first, second);
            
            return std::min(first, second);*/
        }
    }
    if(n % 2 == 0)
    {
        if(k % 2 == 0)
        {
            //ll first = recurse((n / 2), k / 2);
            ll second = recurse((n / 2) - 1, k / 2);
            if(k == 0 && n <= n2)
            {
                //cout << "N k " << n << " " << k << endl;
                n2 = n;
                //large = std::max(first, second);
                ll first = recurse((n / 2), k / 2);
                large = first;
            }
            
            string key = to_string(n) + "_" + to_string(k);
            //mymap[key] = std::min(first, second);
            mymap[key] = second;
            return second;
            //return std::min(first, second);
        }else if(k % 2 == 1)
        {
            //cout << (n / 2) << " " << k / 2 + 1 << endl;
            ll first = recurse((n / 2), k / 2 + 1);
            //cout << (n / 2) - 1 << " " << k/2 << endl;
            //ll second = recurse((n / 2) - 1, k / 2);
            
            string key = to_string(n) + "_" + to_string(k);
            //mymap[key] = std::min(first, second);
            mymap[key] = first;
            //return std::min(first, second);
            return first;
        }
    }
    //cout << "Ran " << endl;
    return -1;
    
}




int main()
{
    ll casses;
    cin >> casses;
    for(int caseNum = 0; caseNum < casses; caseNum++)
    {
        ll n, k;
        mymap.clear();
        prune2Min.clear();
        n2 = 1000000000000000001;
        large = -1;
        cin >> n >> k;
        cout << "Case #" << caseNum + 1 << ": " << large
        << " " << recurse(n,k) << endl;
        
    }

    return 0;
}
