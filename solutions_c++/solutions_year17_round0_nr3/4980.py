#include <bits/stdc++.h>
using namespace std;

vector <int> v;
int main() {
    int n;
    scanf("%d",&n);
    for(int i=0; i<n; i++){
        int t,ktory;
        scanf("%d%d",&t,&ktory);
        v.clear();
        int temp=t;
        v.push_back(temp);
        for(int j=0; j<=ktory; j++){
            temp=v[j];
            if(temp%2==0)
            {
                temp/=2;
                v.push_back(temp);
                if(temp-1!=-1) v.push_back(temp-1);
                else v.push_back(temp);

            }
            else{
                temp/=2;
                v.push_back(temp);
                v.push_back(temp);
            }


        }
        sort(v.begin(),v.end());
        if(v[v.size()-ktory]%2==0)
        {
            printf("Case #%d: %d ",i+1,v[v.size()-ktory]/2);
            if(v[v.size()-1-ktory]!=0){
                printf("%d\n",v[v.size()-ktory]/2-1);
            }
            else printf("%d\n",i+1,v[v.size()-ktory]);

        } else {
            printf("Case #%d: %d ",i+1,v[v.size()-ktory]/2);
            printf("%d\n",v[v.size()-ktory]/2);
        }
    }

    return 0;
}
