#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pii;


#define se second
#define fi first
#define pb push_back
#define mp make_pair

int c[6];
int ic[6];
string str;

bool check() {
    //cout<<(str[0]!=str[str.size()-1])<<endl;
    return (str[0]!=str[str.size()-1]);
}

bool emp() {
    for(int i = 0; i < 6; i++) {
        if(c[i]) {
            return false;
        }
    }
    return (true && check());
}

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    string ch = "RYB";
    for(int testcase = 1; testcase <= t; testcase++) {
        str = "";
        printf("Case #%d: ", testcase);
        int n;
        cin>>n;
        for(int i = 0; i < 6; i++) {
            cin>>c[i];
            ic[i] = c[i];
        }
        int B = c[4]-c[1]-1, R = c[0]-c[3]-1, Y = c[2]-c[5]-1;
        char largest;
        if(B>R && B > Y) {
            largest = 'B';
        } else if(R > Y && R > B) {
            largest = 'R';
        } else {
            largest = 'Y';
        }
        if(c[1]!=0) {
            str +='B';
            c[4]--;
        }
        while(c[1]!=0) {
            c[1]--;
            c[4]--;
            str+="OB";
        }
        if(c[4] <0) {
            c[4]++;
            str.pop_back();
            cout<<(emp()?str:"IMPOSSIBLE\n"); continue;
        }
        if(largest == 'Y' && c[3]!=0 && ic[1] != 0) {
            str+='Y';
            c[2]--;
        }
        if(c[3]!=0) {
            str +='R';
            c[0]--;
        }
        while(c[3]!=0) {
            c[3]--;
            c[0]--;
            str+="GR";
        }
        if(c[0] <0) {
            c[0]++;
            str.pop_back();
            cout<<(emp()?str:"IMPOSSIBLE\n");continue;
        }
        if(largest == 'B' && ic[3]!=0 && c[5] !=0) {
            str+='B';
            c[2]--;
        }
        if(c[5]!=0) {
            str +='Y';
            c[2]--;
        }
        while(c[5]!=0) {
            c[5]--;
            c[2]--;
            str+="VY";
        }
        if(c[2] <0) {
            c[2]++;
            str.pop_back();
            cout<<(emp()?str:"IMPOSSIBLE\n");continue;
        }
        /*for(int i = 0; i < 6; i++) {
            cout<<c[i]<< " ";
        }
        cout<<endl;*/
        priority_queue<pii> pq;
        if(c[0]!=0)
            pq.push({c[0],0});
        if(c[2]!=0)
            pq.push({c[2],1});
        if(c[4]!=0)
            pq.push({c[4],2});
        while(!pq.empty()) {
            pii p1 = pq.top();
            pq.pop();
            if(pq.empty()) {
                if(p1.fi!=1) {
                    str = "IMPOSSIBLE\n";
                    break;
                } else {
                    str += ch[p1.se];
                    break;
                }
            }
            pii p2 = pq.top();
            pq.pop();
            str+= ch[p1.se];
            str+= ch[p2.se];
            if(p1.fi!=1) {
                pq.push({p1.fi-1, p1.se});
            }
            if(p2.fi!=1) {
                pq.push({p2.fi-1, p2.se});
            }
            //cout<<str<<endl;
        }
        if(str[str.size()-1]==str[0]) {
            if(str[str.size()-1]!=str[str.size()-3]) {
                char temp = str[str.size()-1];
                str[str.size()-1] = str[str.size()-2];
                str[str.size()-2] = temp;
            }
        }
        cout<<(check()?str:"IMPOSSIBLE")<<endl;

    }
}