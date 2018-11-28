#include <bits/stdc++.h>
#include <string>
using namespace std;
/*long long N,M,T;
vector<string> varos;
map<string,int> varosid;
vector<int> tav;
vector<vector<int>> komptav;

vector<map<long long,long long>> szamolt;
vector<long long> kov;

long long magic(long long n = 0, long long t = 0, long long val = 0)
{
    if(t>T)
        return -100000000;
    if(n == N)
        return val;
    if(szamolt[n][t] != 0)
        return szamolt[n][t];

    int maxval = 0;

    //kompok N-1-ig
    for(int i = n+1;i<N;i++)
    {
        if(komptav[n][i] != 0)
        {
            if(magic(i,t+komptav[n][i],val)>maxval){
                maxval = magic(i,t+komptav[n][i],val);
                kov[n] = i;
            }
        }
    }
    //komp N-hez
    if(komptav[n][0] != 0)
    {
        if(magic(N,t+komptav[n][0],val)>maxval){
            maxval = magic(N,t+komptav[n][0],val);
            kov[n] = 0;
        }
    }

    //bicikli/szoporoller
    if(magic(n+1, t+tav[n],val+tav[n]) > maxval){
        maxval = magic(n+1, t+tav[n],val+tav[n]);
        kov[n] = n+1;

    }
    szamolt[n][t] = maxval;
    return maxval;
}


int main()
{

    cin >> N;
    komptav.resize(N);
    varos.resize(N);
    tav.resize(N);
    kov.resize(N);
    szamolt.resize(N);
    for(int i = 0;i<N;i++){
        cin >> varos[i];
        varosid[varos[i]] = i;
        komptav[i] = vector<int>(N);

    }
    for(int i = 0;i<N;i++){
     cin >> tav[i];
    }
    cin >> M;
    string v1, v2;
    int ar;
    for(int i = 0;i<M;i++){
        cin >> v1 >> v2 >> ar;
        komptav[varosid[v1]][varosid[v2]] = ar;
        //komptav[varosid[v2]][varosid[v1]] = ar;
    }
    cin >> T;

    cout << magic() << endl;
    int jelen = 0;
    while(jelen != N)
    {
        if(kov[jelen] - jelen > 1){
            assert(komptav[jelen][kov[jelen]] != 0);
            cout << varos[jelen] << " " << varos[kov[jelen]] << " " <<komptav[jelen][kov[jelen]] << endl;
        }
        jelen = kov[jelen];
    }
    return 0;
}
*/
string state;
void flop(int from, int to){
    for(int i=from;i<to;i++)
    {
        if(state[i]=='-') state[i]='+';
        else state[i]='-';
    }
}


int main()
{
    int T;
    cin >> T;
    string lol;
    for(int t = 0;t<T;t++)
    {
        int flopnum = 0;

        int floplen;
        cin >> state >> floplen;
        int i = 0;
        while(i<state.size()-floplen+1)
        {
            if(state[i]=='-')
            {
                flop(i,i+floplen);
                flopnum++;
                //cout << "FLOP: " <<i << " " <<state << endl;
            }

            i++;
        }
        int bad = false;
        for(int i = 0;i<state.size();i++)
        {
            if(state[i]=='-')
                bad = true;
        }
        cout << "Case #"<< t+1 <<": " ;
        if (!bad) cout << flopnum; else cout << "IMPOSSIBLE";
        cout <<endl;
    }
    return 0;
}
