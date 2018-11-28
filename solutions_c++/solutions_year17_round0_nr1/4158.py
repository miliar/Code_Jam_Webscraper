#include <iostream>
#include <string>
#include <stdio.h>
#include <cstring>
#include <fstream>

using namespace std;
int t,k,ans;
string s;
ofstream answer;

int main()
{
    answer.open("answer.txt");
    scanf("%d",&t);
    for (int i=0;i<t;i++){
        cin >> s >> k;
        int w=s.size();
        for (int j=0;j<w;j++){
            if (s[j]=='-' && j<=w-k){
                for (int q=0;q<k;q++){
                    if (s[j+q]=='-') s[j+q]='+';
                    else s[j+q]='-';
                }
                ans++;
            }else if (s[j]=='-'){
                ans=-1;
                break;
            }
        }
        if (ans==-1) answer<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        else answer<<"Case #"<<i+1<<": "<<ans<<endl;
        ans=0;
    }
    answer.close();
    return 0;
}
