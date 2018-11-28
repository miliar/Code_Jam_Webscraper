#include<bits/stdc++.h>

using namespace std;
int n,k;
int res1, res2;
vector<int> s,s2;

void push(int num, int count){
    int vt = s.size()-1;
    if (s[vt]!=num) {
        s.push_back(0);
        s2.push_back(0);
        vt++;
    }
    s[vt] = num;
    s2[vt]+=count;
}

int main(){
    freopen("C-small-2-attempt0.in","r",stdin);    

    freopen("C-small-1-attempt0.out","w",stdout);    
    int T;
    cin>>T;
    int T2= T;
    while(T--){
        cin>>n>>k;
        s.clear();
        s2.clear();
        s.push_back(n);
        s2.push_back(1);
        int bot = 0;
        while(k>0){
            if (s[bot]&1){
                push(s[bot]/2,s2[bot]*2);
                k-=s2[bot];
                if (k<=0){
                    res1=res2=s[bot]/2;
                }
            }
            else{
                push(s[bot]/2,s2[bot]);
                push(s[bot]/2-1,s2[bot]);
                k-=s2[bot];
                if (k<=0){
                    res1 = s[bot]/2;
                    res2 = s[bot]/2-1;
                }
            }
            bot++;
        }
        printf("Case #%d: %d %d\n",T2-T,res1, res2);
    }
}
