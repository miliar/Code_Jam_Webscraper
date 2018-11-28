#include <iostream>
#include <vector>
#include <string>
using namespace std;

int convert(char c)
{
    if(c == '+') return 1;
    return 0;
}

void flipper(vector<int>& v, int position, int k){
    if(position + k > (int)v.size())
    {
        cout << "ERROR INVALID FLIPPPER POSITION:\n";
        for(int i = 0; i  < (int)v.size(); i++)
            cout<< v[i];
        cout <<"\n";
        cout << "pos:" << position << " k:"  << k << "\n";
        cout << "v.size():" << (int)v.size() << "\n";
        cout << "delta:" << position - ((int)v.size()-k) << "\n";
        return;
    }
    for(int i = 0; i < k; i++)
    {
        v[i+position] = (v[i+position] + 1) % 2;
    }
}

int solver(vector<int>& v, int k){
    int counter = 0;
    for(int i = 0; i <= (int)v.size()-k; i++)
    {
        if(v[i] != 1){
            flipper(v,i,k);
            counter++;
        } 
    }
    for(int i = 0; i < (int)v.size(); i++)
    {
        if(v[i] == 0) return -1;
    }
    return counter;
}

int main(){
    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
    {

        vector<int> v;
        string s;
        int k;
        cin >> s >> k;
        v.reserve(s.size());
        for(int j = 0; j < (int)s.size(); j++)
        {
            v.push_back(convert(s[j]));
        }
        int sol = solver(v,k);
        cout << "Case #" << i+1 << ": ";
        if(sol == -1) cout << "IMPOSSIBLE\n";
        else cout << sol << "\n";
    }
}