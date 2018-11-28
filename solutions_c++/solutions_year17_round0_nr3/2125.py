#include <bits/stdc++.h>
using namespace std;

#define boost ios_base::sync_with_stdio(0)
#define endl '\n'
#define tab '\t'
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


    ifstream input ("C-large.in");
    ofstream output;
    output.open("C-large-output.in");
    if (input.is_open()&& output.is_open())
    {
        int t;
        input>>t;
        string temp;
        //cout<<t<<endl;
        //getline(input, temp);
        int kl =1;
        for(int index=0;index<t;++index){
            ull n, k;
            input>>n>>k;
            //cout<<n<<"\t"<<k<<endl;
            ull high=0, low=0;
            ull hcount=0, lcount=0;
            ull num = n;
            ull rs=0, ls=0;
            if(num%2 == 0){
                high = num/2;
                low = high-1;
            }else{
                high = low = num/2;
            }
            if(k==1){
                rs = high;
                ls = low;
            }else{
                --k;
                hcount = 1;
                lcount = 1;

                while(k!=0){
                    //cout<<high<<tab<<low<<tab<<hcount<<tab<<lcount<<tab<<k<<endl;
                    if(hcount+lcount >= k){
                        break;
                    }else{
                        k = k - hcount - lcount;
                    }
                    if(high == low){
                        if(high%2==0){
                            high = high/2;
                            low = high - 1;
                            hcount = hcount*2;
                            lcount = lcount*2;
                        }else{
                            high = high/2;
                            low = (low/2);
                            hcount = hcount*2;
                            lcount = lcount*2;
                        }
                    }else if(high%2 == 0){
                        high = high/2;
                        low = high - 1;
                        hcount = hcount;
                        lcount = (lcount*2)+hcount;
                    }else if(high%2 != 0){
                        high =  high/2;
                        low = high - 1;
                        lcount = lcount;
                        hcount = lcount + (hcount*2);
                    }
                }
                //cout<<high<<tab<<low<<tab<<hcount<<tab<<lcount<<tab<<k<<endl;

                if(k<=hcount){
                    if(high%2 == 0){
                        rs = high/2;
                        ls = rs-1;
                    }else{
                        rs = ls = high/2;
                    }
                }else{
                    if(low%2 == 0){
                        rs = low/2;
                        ls = rs-1;
                    }else{
                        rs = ls = low/2;
                    }
                }
            }

            //cout<<"Case #"<<kl<<": "<<max(rs, ls)<<" "<<min(rs, ls)<<endl;
            output<<"Case #"<<kl<<": "<<max(rs, ls)<<" "<<min(rs, ls)<<endl;
            ++kl;
        }



        input.close();
        output.close();
    }


    return 0;
}


