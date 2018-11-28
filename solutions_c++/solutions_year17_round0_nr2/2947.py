#include <bits/stdc++.h>
using namespace std;

char str[55];

int main(){

	int t , idx;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d",&t);
	for(int T = 1 ; T <= t ; ++T){
        scanf("%s",str);
        string s = string(str);
        bool flag = true;
        for(int i = 0 ; i < s.size()-1 && flag; i++)
            if(s[i+1] < s[i]){
                flag = false;
                idx = i;
            }


        if(!flag){
            for(int i = idx + 1 ; i < s.size() ; i++)
                s[i] = '9';

            while(idx){
                s[idx]--;
                if(s[idx] >= s[idx-1])
                    break;
                s[idx] = '9';
                idx--;
            }

            if(!idx){
                if(s[idx] == '1')s.erase(0,1);
                else s[idx]--;
            }
        }

        printf("Case #%d: %s\n",T,s.c_str());
	}

	return 0;
}
