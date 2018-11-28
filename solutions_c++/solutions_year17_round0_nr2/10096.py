#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
//#define _DEBUG
int test_case;
using namespace std;
bool isTidy(long long int t)
{
    if(t<10)
    return true;
    vector<int> v,vv;
    while(t/10){
        v.push_back(t%10);
        vv.push_back(t%10);
        t/=10;
    }
    v.push_back(t);
    vv.push_back(t);
    sort(v.begin(), v.end(), greater<int>());
    #ifdef _DEBUG
    cout << "V :";
    for(vector<int>::iterator it = v.begin(); it!=v.end(); it++)
    cout << *it << " ";
    cout << endl;
    cout << "VV :";
    for(vector<int>::iterator it = vv.begin(); it!=vv.end(); it++)
    cout << *it << " ";
    cout << endl;
    #endif
    for(int i = 0 ; i < v.size(); i++)
    {
        if(v[i] !=vv[i])
        return false;
    }
    return true;
}
long long int N;
int main()
{
    cin >> test_case;
    for(int T = 1; T <= test_case; T++)
    {
        cin >> N;
        while(1)
        {
            if(!isTidy(N))
              N--;
            else
              break;
        }
        cout << "Case #"<<T<<": "<<N<<endl;
    }
    return 0;
}