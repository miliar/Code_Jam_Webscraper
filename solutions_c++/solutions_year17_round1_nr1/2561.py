#include <iostream>

using namespace std;

int T,R,C;
char arr[26][26];
char result[26][26];
char in[26];
int cnt=0;
char *msg = "Case #";
void getResult();

int main() {

    cin>>T;
    for(int t=1;t<=T;t++) {
        cnt=0;
        cin>>R>>C;
        for(int r=1;r<=R;r++){
            for(int c=1;c<=C;c++){
                cin>>arr[r][c];
            }
        }
        getResult();
        cout<<msg<<t<<":"<<endl;
         for(int r=1;r<=R;r++){
            for(int c=1;c<=C;c++){
                    cout<<arr[r][c];
            }
            cout<<endl;
         }

    }
    return 0;
}

void getResult(){
   //row

   for(int r=1;r<=R;r++) {
            for(int c=1;c<C;c++){
            if(arr[r][c]!='?' && arr[r][c+1]=='?')
                arr[r][c+1] = arr[r][c];

            else if(arr[r][c]=='?' && arr[r][c+1]!='?')
                arr[r][c]=arr[r][c+1];
            }

            for(int c=C;c>1;c--) {
                if(arr[r][c]!='?' && arr[r][c-1]=='?')
                arr[r][c-1] = arr[r][c];

            else if(arr[r][c]=='?' && arr[r][c-1]!='?')
                arr[r][c]=arr[r][c-1];
            }
   }



   for(int c=1;c<=C;c++){
          for(int r=1;r<R;r++){
             if(arr[r][c]!='?' && arr[r+1][c]=='?')
                    arr[r+1][c]=arr[r][c];
             else if(arr[r][c]=='?' && arr[r+1][c]!='?')
                    arr[r][c]=arr[r+1][c];
           }

           for(int r=R;r>1;r--){
             if(arr[r][c]!='?' && arr[r-1][c]=='?')
                    arr[r-1][c]=arr[r][c];
             else if(arr[r][c]=='?' && arr[r-1][c]!='?')
                    arr[r][c]=arr[r-1][c];
           }
   }
}
