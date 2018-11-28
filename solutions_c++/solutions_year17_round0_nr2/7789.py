#include <bits/stdc++.h>
using namespace std;
bool jo(int x)
{
    vector<int> je;
    while(x>0)
    {
        je.push_back(x%10);
        x/=10;
    }
    for(int u=0; u<je.size()-1; u++)
    {
        if(je[u]<je[u+1]) return false;
    }
    return true;
}
int test;
int n;
int main()
{
    cin>>test;
    for(int tt=1; tt<=test; tt++)
    {
        cin>>n;
        while(!jo(n)) n--;
        cout<<"Case #"<<tt<<": "<<n<<endl;
    }
    return 0;
}
