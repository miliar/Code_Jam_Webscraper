#include<bits/stdc++.h>
#define s(x) scanf("%d",&x)
#define ll long long
#define l(x) scanf("%I64d",&x)
#define cst int t; s(t); while(t--)
#define fr freopen("A-large.in", "r", stdin)
#define fo freopen("out.txt", "w", stdout)
#define finp ios_base::sync_with_stdio(false)
#define pb push_back
#define pf printf

using namespace std;

int pancake(string S, int K)
{
    int cnt=0;
    bool flag=0;
    for(int i=0; i<S.length()-K+1; i++)
        if(S[i] == '-'){
            int j=i;
            while(j< K+i){
                if(S[j] == '-')
                    S[j] = '+';
                else
                    S[j] = '-';
                j++;
            }
            cnt++;
        }
    for(int i=S.length()-K; i<S.length(); i++)
        if(S[i] == '-'){
            flag = true;
            break;
        }
    if(flag)
        return -1;
    return cnt;
}

int main()
{
    fr;
    fo;
    int t;
    cin>>t;
    for(int caseNo=1; caseNo<=t; caseNo++){
        string S;
        int K;
        cin>>S>>K;
        int cnt = pancake(S, K);
        if(cnt == -1)
            printf("Case #%d: IMPOSSIBLE\n", caseNo);
        else
            printf("Case #%d: %d\n", caseNo, cnt);
    }
    return 0;
}

