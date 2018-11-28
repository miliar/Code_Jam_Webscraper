/* 
 * Prob:  
 * Author: sameerpandit
 *
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>
#include <map>

using namespace std;

int main() {
    int T;
    cin>>T;
    int t = T;
    while (T--) {
        string s;
        int k;
        cin>>s>>k;
        cout << "Case #" << t - T << ": ";
        int n=s.size()-k+1;
        string flipped(s.size(),'+');
        if(flipped==s){
            cout<<0<<endl;
            continue;
        }
        int ans=0;
        for(int i=0;i<(1<<n);i++){
            string flipped(s.size(),'+');                           
            int num=i;
            while(num){
                int t=num-1;
                t=t&num;
                int temp=(t^num);
                int pos=-1;
                while(temp){
                    temp>>=1;
                    pos++;
                }
                num&=(num-1);
                ans++;
                for(int j=0;j<k;j++){
                    int realPos=j+pos;
                    flipped[realPos]=flipped[realPos]=='+'?'-':'+';
                }
//                cout<<"pos: "<<pos<<" "<<flipped<<" ";
            }
//            cout<<endl;
            if(flipped==s){
                cout<<ans; 
                break;
            }else{
                ans=0;
            }            
        }
        if(ans==0)
            cout<<"IMPOSSIBLE";
        cout << endl;
    }
    return 0;
}
