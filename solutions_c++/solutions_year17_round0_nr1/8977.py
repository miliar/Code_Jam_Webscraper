// In the name of Allah the Most Merciful.

#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

string ar;
int si , k;

bool is_ok(string ar)
{

    int si = ar.size();

    for(int i=0;i<si;i++)if(ar[i]!='+')return false;

    return true;
}

int f()
{

    int i = 0 , counter1 = 0;
    string temp = ar;

    while(i+k-1<si){
    //cout << i+k << " " << si+1 << endl;

        if(temp[i]=='-'){

            for(int j=i;j<i+k;j++){if(temp[j]=='+')temp[j]='-';else temp[j]='+';}
            counter1++;
        }
        i++;
    }

    if(is_ok(temp)==false)counter1=1234567;
    //cout << temp << endl;

    temp = ar;
    reverse(temp.begin() , temp.end());
    int counter2 = 0;
    i = 0;

    while(i+k-1<si){

        if(temp[i]=='-'){

            for(int j=i;j<i+k;j++){if(temp[j]=='+')temp[j]='-';else temp[j]='+';}
            counter2++;
        }

        i++;
    }

    if(is_ok(temp)==false)counter2 = 1234567;
    //cout << temp << endl;

    return min(counter1 , counter2);

}

int main(void)
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int i=0;i<t;i++){

        cin >> ar >> k;
        si = ar.size();
        int temp = f();
        if(temp!=1234567)printf("Case #%d: %d\n",i+1 ,temp);
        else printf("Case #%d: IMPOSSIBLE\n",i+1 ,temp);

    }

    return 0;
}
