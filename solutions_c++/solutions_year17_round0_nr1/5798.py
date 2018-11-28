#include<iostream>
#include<fstream>
using namespace std;
int t, k, curFl, flips[1001], nFlips;
bool poss;
string s;
int main()
{
    ifstream cin;
    ofstream cout;
    cin.open("A-large.in");
    cout.open("out.txt");
    cin>>t;
    for(int o=1; o<=t; o++) {
        cin>>s>>k;
        for(int i=0; i<s.size(); i++) flips[i] = 0;
        curFl = 0;
        poss = true;
        nFlips = 0;
        for(int i=0; i<s.size(); i++) {
            if(flips[i] == 1) curFl--;
            int p;
            if(s[i] == '+') {
                p=1;
            }
            else p=0;
            p = (p+curFl)%2;
            if(p == 0) {
                if(s.size()-i < k) {
                    poss = false;
                    break;
                }
                curFl++;
                nFlips++;
                flips[i+k]=1;
            }
        }
        cout<<"Case #"<<o<<": ";
        if(poss) cout<<nFlips<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    cin.close();
    cout.close();
    return 0;
}
