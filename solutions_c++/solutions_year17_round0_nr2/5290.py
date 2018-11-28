#include <iostream>
#include <string.h>
using namespace std;

int tidy1(int x){
    int l=9;

    while(x){
        if(x%10<=l){
            l=x%10;
        }
        else return false;

        x/=10;
    }

    return true;
}

int tidy2(int x){
    while(!tidy1(x))x--;
    return x;
}

char *clean(char* x){
    while(x[0]=='0'){x++;}
    return x;
}

char* tidy(char* x){
    char l='9';
    int lm=1000;

    for(int i=strlen(x)-1;i>=0;i--){
        if(x[i]==l && lm == i+1){
            lm--;
            continue;
        }

        if(x[i] > l){
            lm=i;
        }
        l = x[i];
    }
    char *nr = new char[20];

    for(int i=strlen(x)-1;i>=0;i--){
        if(i>lm)nr[i]='9';
        else if(i==lm){
            nr[i]=x[i]-1;
        }
        else nr[i] =x[i];
    }

    nr[strlen(x)] = '\0';
    return clean(nr);
}

int main()
{
    int t;
    cin>>t;

    for(int i=1;i<=t;i++){
        char n[20];
        cin>>n;
        cout<<"Case #"<<i<<": "<<tidy(n)<<"\n";
    }

    return 0;
}
