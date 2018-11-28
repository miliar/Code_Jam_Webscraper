#include <bits/stdc++.h>
using namespace std;

ifstream be ("Codejam1Ca.txt");
ofstream ki ("Codejam1Caout.txt");
vector<double> megoldas;

double PI=3.1415926535897;

void process()
{
    int n,k;
    be>>n>>k;
    double maxarea=0;
    vector<pair<double, double> > pancakes;
    for(int i=1;i<=n;i++)
    {
        double r,h;
        be>>r>>h;
        pancakes.push_back({-r,-h});
    }
    sort(pancakes.begin(),pancakes.end());
    for(int i=0;i<=pancakes.size()-k;i++)
    {
        //cout<<-pancakes[i].first<<" "<<-pancakes[i].second<<endl;
        //cout<<i<<endl;
        pancakes[i].first*=-1;
        pancakes[i].second*=-1;
        //cout<<pancakes[i].first<<" "<<pancakes[i].second<<"***   ";
        double aktarea=0;
        aktarea+=PI*pancakes[i].first*pancakes[i].first;
        aktarea+=2*PI*pancakes[i].second*pancakes[i].first;
        vector<double> high;
        for(int j=i+1;j<pancakes.size();j++)
        {
            high.push_back(-2*PI*pancakes[j].second*pancakes[j].first);
        }
        sort(high.begin(),high.end());
        //reverse(high.begin(),high.end());

        for(int j=0;j<k-1;j++)
        {
            //cout<<-high[j].first<<" "<<-high[j].second<<endl;
            aktarea+=-high[j];
        }
        //cout<<aktarea<<" ";
        maxarea=max(maxarea,aktarea);
    }
    megoldas.push_back(maxarea);
    //cout<<endl<<endl;
}

int t;

int main()
{
    ios_base::sync_with_stdio(false);
    be>>t;
    for(int i=1;i<=t;i++) process();
    for(int i=0;i<megoldas.size();i++)
    {
        ki<<fixed<<setprecision(17)<<"Case #"<<i+1<<": "<<megoldas[i]<<endl;
    }
    return 0;
}
