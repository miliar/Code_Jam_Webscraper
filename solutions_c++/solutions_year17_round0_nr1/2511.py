#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

int main(){
    int c=0,T,K,ans;
    cin >> T;
    string S;
    bool s[1000+10];
    int length,left,right;
    while(c++<T){
        left = right = ans=0;
        cin >> S;
        cin >> K;
        length = S.length();
        for(int i=0;i<S.length();i++){
            s[i] = S[i] == '-' ? 0 : 1;
        }

        for(int i=0;i<length;i++){
            if(!s[i]){
                left = i;
                break;
            }
        }

        for(int i=length-1;i>=left;i--){
            if(!s[i]){
                right = i ;
                break;
            }
        }
        //cout << left << right<<endl;
        while(left<length && right >=0 && right - left >= K-1){

            for(int i=left+K-1;i>=left;i--)
                s[i] = !s[i];

            if(!s[right]){
                for(int i=right-K+1;i<=right;i++)
                    s[i] = !s[i];
                ans++;
            }

            while(left<length && s[left]) left++;
            while(right>=0 && right>= left && s[right]) right--;
            ans++;
//            for(int i=0;i<length;i++)
//                cout << s[i] << ' ';
//            cout<<endl;
//            cout << left << right<<endl;
        }
        bool k = true;
        for(int i=0;i<length;i++)
            k = k&&s[i];

        if(k) printf("Case #%d: %d\n",c,ans);
        else printf("Case #%d: IMPOSSIBLE\n",c);
    }

    return 0;
}
