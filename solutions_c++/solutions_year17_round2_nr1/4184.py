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


bool sortcol( const vector<int>& v1,
               const vector<int>& v2 ) {
 return v1[0] < v2[0];
}
int main()
{
    boost;cin.tie(0),cout.tie(0);


    ifstream input ("A-small-attempt3.in");
    ofstream output;
    output.open("A-small-output.in");
    if (input.is_open()&& output.is_open())
    {
        int t;
        input>>t;
        string temp;
        getline(input, temp);
        int kl =1;
        for(int index=0;index<t;++index){
            int d,n;
            input>>d>>n;
            getline(input, temp);
            vector<vector<int> > det(n, vector<int>(2));
            for(int i=0;i<n;++i){
                int a;
                input>>a;
                det[i][0] = a;
                input>>a;
                det[i][1] = a;
                getline(input, temp);
            }
            sort(det.begin(), det.end());

            double time = (double)(d-det[0][0])/(double)det[0][1];
            double lastspeed = 0;
            for(int i=1;i<n;++i){
                if(det[i][1]<det[lastspeed][1]){
                    double v2,v1,s2,s1;
                    v2=det[i][1];
                    s2=det[i][0];
                    v1 = det[lastspeed][1];
                    s1 = det[lastspeed][0];
                    double x = ((v2*s1)-(v1*s2))/(v2-v1);
                    double time2 = (x-s2)/v2;
                    if(time2<time){
                        time2+=(d-x)/v2;
                        time=time2;


                    }

                    lastspeed = i;

                }
            }

            double maxspeed = (double)d/(double)time;
            //cout<<"Case #"<<kl<<": "<<max(rs, ls)<<" "<<min(rs, ls)<<endl;
            output<<"Case #"<<kl<<": "<<std::fixed<<setprecision(6)<<maxspeed<<endl;
            ++kl;
        }

        input.close();
        output.close();
    }


    return 0;
}


