#include <iostream>

using namespace std;


string solve(string maxi,int index=0,int last=0){
    if (index == maxi.length()) return maxi;
    if(maxi[index] >= last)
        return solve(maxi,index+1,maxi[index]);
    else {

        maxi[index-1]--;
        for (int i=index-1 ; i > 0 ;i--)
                if(maxi[i] < maxi[i-1])
                     maxi[i-1]--,maxi[i]='9';

        for(int i =index ; i < maxi.length() ; i++)
            maxi[i]='9';

        return solve(maxi,index,maxi[index-1]);
    }
}


int main() {
    string maxi;
    bool pr;
    int T,i,k,t ;
    scanf("%d", &T);
   for (t=0 ;t < T;t++) {
       pr=false;
       cin >> maxi;
       printf("Case #%d: ", t+1);
       maxi=solve(maxi);
       for(i =0 ; maxi[i]!='\0';i++ )
           if(maxi[i] !='0' || pr)
                putchar(maxi[i]),pr=true;

       if(t != T-1)
           printf("\n");
    }
}

