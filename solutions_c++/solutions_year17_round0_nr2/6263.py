#include <bits/stdc++.h>
using namespace std;
int n;
string rb;
int conv(char r)
{
    return r - '0';
}
void process(string &ss, int casee)
{
    if(ss.size()==1)
    {
        cout << "Case #" << casee << ":" << " " << ss << '\n';
        return;
    }
    int lm = ss.size();
    int tv = -1;
    for(int i=0;i<lm-1;i++)
    {
        if(conv(ss[i])>conv(ss[i+1]))
        {
            tv=i;
            break;
        }
    }
    if(tv==-1)
    {
       cout << "Case #" << casee << ":" << " " << ss << '\n';
       return;
    }
    int rt = -1;
    for(int i=tv-1;i>=0;i--)
    {
        if(conv(ss[i])<conv(ss[i+1])){
            rt = i;
            break;
        }
    }
    if(rt==-1)
    {
        rt = 0;
    }
    else{
        rt++;
    }
    //print as is till the change point
    cout << "Case #" << casee << ":" << " ";
    for(int i=0;i<rt;i++){
        cout << ss[i];
    }
    if(conv(ss[rt])==1){
        for(int i=rt+1;i<lm;i++){
            cout << 9;
        }
    }
    else{
        cout << conv(ss[rt])-1;
        for(int i=rt+1;i<lm;i++){
            cout << 9;
        }
    }
    cout << '\n';
}
int main()
{
    freopen("tidin.txt","r",stdin);
    freopen("tidout.txt","w",stdout);
    cin.tie(0),cout.tie(0),ios_base::sync_with_stdio(false);
    cin >> n;
    for(int i=0;i<n;i++)
    {
        cin >> rb;
        process(rb,i+1);
    }
    return 0;
}
