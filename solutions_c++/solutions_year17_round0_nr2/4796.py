#include <bits/stdc++.h>
using namespace std;

bool istidy(string o){
    int mini=100;
    for(int p=o.size()-1; p>=0; p--){

        if(int(o[p]>mini)) return 0;
        else mini=int(o[p]);
    }
    return 1;
}
int main() {
    int t;
    string str;
    scanf("%d",&t);
    int last=0;
    for(int i=1; i<=t; i++){
        cin>>str;
        if(!istidy(str)){
            while(!istidy(str)){
              last=0;

              for(int j=str.size()-1; j>=0; j--){

                  if(int(str[j])>int(str[j+1])){
                      last=j;
                  }
              }
              if(last!=str.size()-1)
              {
                  str[last]-=1;
                  for(int c=last+1; c<str.size(); c++){
                      str[c]=char(57);
                  }
              }

            }
            printf("Case #%d: ",i);
            bool rep=0;
            for(int c=0; c<str.size(); c++){
                if((int(str[c])!=48)or(rep==1))
                {
                    rep=1;
                    printf("%c",str[c]);
                }

            }
            printf("\n");
        }
        else {
            printf("Case #%d: ",i);
            cout<<str<<"\n";
        }

    }

    return 0;
}
