#include <bits/stdc++.h>
using namespace std;
vector <bool> v;
int main() {
    string str;
    int n;
    scanf("%d",&n);
    int s;
    for(int i=0; i<n; i++){
        getchar();
        cin>>str;
        v.clear();
        scanf("%d",&s);
        for(int j=0; j<str.size(); j++){
            if(str[j]=='+') v.push_back(1);
            else v.push_back(0);
        }
        bool flipped=0;
        int wynik=-1;
        bool niewyp=0;
        while((!flipped)and(niewyp==0))
        {
            wynik++;
            flipped=1;
            for(int j=0; j<v.size(); j++){
                if(v[j]==0) {
                    flipped=0;
                    for(int c=j; c-j<=(s-1); c++)
                    {
                        if(c>v.size()-1) {
                            printf("Case #%d: IMPOSSIBLE\n",i+1);
                            niewyp=1;
                            break;
                        }
                        v[c]=!v[c];
                    }
                    break;
                }

            }
        }
        if(niewyp==0)printf("Case #%d: %d\n",i+1,wynik);

    }

    return 0;
}