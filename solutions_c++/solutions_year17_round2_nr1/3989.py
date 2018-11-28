using namespace std;

int main(){
    int T;
    cin >> T;
    for(int a0 = 0; a0 < T; a0++){
        cout<<"Case #"<<a0+1<<": ";
        int d;
        int n;
        double max=0;
        cin >> d >> n;
        for (int a1=0;a1<n;a1++){
            int k;
            int s;
            cin>>k >>s;
            double temp=(double)(d-k)/(double)s;
            cerr<<"temp: "<<temp<<endl;
            if (temp>max){
                max=temp;
            }
        }
        cerr<<"d: "<<d<<"max: "<<max<<endl;
        cout<<(double)d/(double)max<<endl;
        
        
    }
    return 0;
}
