#include <bits/stdc++.h>
using namespace std;

#define boost ios_base::sync_with_stdio(0)
#define endl '\n'
#define ll long long
#define ull unsigned long long
#define max(a,b) ((a>b)?(a):(b))
#define min(a,b) ((a<b)?(a):(b))

//constants
#define MAX 100005
#define inf LLONG_MAX
#define MIN INT_MIN
#define PIE 3.141592653589793238

ll mod=1e9+7;
ll gcd(ll a , ll b){return b==0?a:gcd(b,a%b);}



int main()
{
    boost;cin.tie(0),cout.tie(0);

    ifstream input ("A-large.in");
    ofstream output;
    output.open("A-large-output.in");
    if (input.is_open()&& output.is_open())
    {
        int t;
        input>>t;
        string temp;
        getline(input, temp);
        int kl =1;
        while(t--){
            string seq;
            input>>seq;
            int k;
            input>>k;
            getline(input, temp);

            int n = seq.length();
            int firstm=-1;
            int c = 0, im =0;
            for(int i = 0;i<n;++i){
                    //cout<<seq<<endl;
                if(seq[i]=='-'){
                        firstm =-1;
                    if(i+k-1>=seq.length()){
                        im=1;
                        //cout<<"not suffcient chars\n";
                        break;
                    }
                    for(int j=i;j<=i+k-1;++j){
                        if(seq[j]=='-'){
                            seq[j]='+';
                        }else{
                            seq[j]='-';
                            if(firstm==-1){
                                firstm=j;
                            }
                        }
                    }
                    if(firstm ==-1)
                        i += (k-1);
                    ++c;
                }else{
                    if(firstm!=-1){
                         i = firstm-1;
                         //cout<<i<<endl;
                    }

                    firstm = -1;
                }
            }

            for(int i = 0;i<n;++i){
                if(seq[i]=='-'){
                    im=1;
                    //cout<<"found minus\n";
                    break;
                }
            }
            if(im){
                    //cout<<"Case #"<<kl<<": "<<"IMPOSSIBLE"<<endl;
                output<<"Case #"<<kl<<": "<<"IMPOSSIBLE"<<endl;
            }else{
                //cout<<"Case #"<<kl<<": "<<c<<endl;
                output<<"Case #"<<kl<<": "<<c<<endl;
            }

            ++kl;


        }



        input.close();
        output.close();
    }


    return 0;
}
