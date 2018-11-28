#include <bits/stdc++.h>
using namespace std;
#define INPUT freopen("in.txt","r",stdout);
#define OUTPUT freopen("out.txt","r",stdout);
#define f first
#define s second
#define pb push_back
#define mp make_pair
typedef long long ll;

const int MAX = 26;
int n,m;
string s[MAX];


vector<pair<char,int> > getConf(int i){
    vector<pair<char,int> > conf;
    for(int j=0;j<m;j++){
        int k = j;
        int cnt = 0;
        while(k < m && s[i][k] == s[i][j]) cnt++,k++;
        j = k-1;
        conf.push_back(mp(s[i][j], cnt));
    }
    return conf;
}

void apply(vector<pair<char,int> > v, int i){
    int idx = 0;
    for(int j=0;j<(int)v.size();j++){
        while(v[j].second--){
            s[i][idx++] = v[j].first;
        }
    }
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,tc(1);
	cin >> T;
	while(T--){
        cin >> n >> m;
        for(int i=0;i<n;i++){
            cin >> s[i];
            for(int j=0;j<m;j++){
                if(s[i][j] != '?'){
                    int k = j-1;
                    while(k>=0 && s[i][k] == '?') s[i][k--] = s[i][j];
                    k = j+1;
                    while(k<m && s[i][k] == '?') s[i][k++] = s[i][j];
                }
            }
        }
        int i = 0;
        while(i<n && s[i][0] == '?') i++;
        int f = i;
        i--;
        if(i >= 0){
            while(i>=0){
                apply(getConf(f), i);
                i--;
            }
        }
        for(int i=0;i<n;i++){
            if(s[i][0] == '?')
                apply(getConf(i-1), i);
        }
        cout << "Case #" << tc++ << ":\n";
        for(int i=0;i<n;i++)
            cout << s[i] << endl;
//        cout << "done" << endl;
	}
    return 0;
}



