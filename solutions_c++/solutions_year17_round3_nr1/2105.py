#include<iostream>
#include<stdio.h>
#include<vector>
#include<map>
#include<algorithm>
#include<fstream>
#include<string>
#include<cstring>
#include<list>
#include<stack>
#include<unordered_set>
#include <iomanip>
#define INF 1000000
#define V 10
#define SIZE 100

using namespace std;
int dist[V][V];

bool bpm(bool bpGraph[SIZE][SIZE], int u, bool seen[], int matchR[])
{
    for (int v = 0; v < SIZE; v++)
    {
        if (bpGraph[u][v] && !seen[v])
        {
            seen[v] = true; // Mark v as visited
            if (matchR[v] < 0 || bpm(bpGraph, matchR[v], seen, matchR))
            {
                matchR[v] = u;
                return true;
            }
        }
    }
    return false;
}

int maxBPM(bool bpGraph[SIZE][SIZE])
{
    int matchR[SIZE];

    memset(matchR, -1, sizeof(matchR));

    int result = 0; // Count of jobs assigned to applicants
    for (int u = 0; u < SIZE; u++)
    {
        bool seen[SIZE];
        memset(seen, 0, sizeof(seen));

        if (bpm(bpGraph, u, seen, matchR))
            result++;
    }
    return result;
}

void apsp (int graph[][V])
{
    memset(dist,0,sizeof(dist));
    int i, j, k;
    for (i = 0; i < V; i++)
        for (j = 0; j < V; j++)
            dist[i][j] = graph[i][j];
    for (k = 0; k < V; k++)
    {
        for (i = 0; i < V; i++)
        {
            for (j = 0; j < V; j++)
            {
                if (dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
            }
        }
    }
    return;
}


/*
Author: Utkarsh Verma
Email ID: utkarsh13103453cse@gmail.com
Contact: +91 9871271616

*/

double maxi(double a,double b){
    if(a>=b){
    return a;
    }else{
    return b;
    }
}

double func(vector< pair< double, double> > &cakes,int N,int K,int done,double area,double last_rad,int now){
    double pi=3.14159265358979;
    if(done==K){
    return area;
    }
    if(now==N){
    return -1;
    }


        if(cakes[now].first<=last_rad){
            double new_area=area;

            if(area>0){

            new_area+=((double)2*pi*cakes[now].first*cakes[now].second);
            }else{

            new_area+=(((double)2*pi*cakes[now].first*cakes[now].second)+(pi*cakes[now].first*cakes[now].first));
            }
            return(maxi(func(cakes,N,K,done+1,new_area,cakes[now].first,now+1),func(cakes,N,K,done,area,last_rad,now+1)));
        }else{

            return(func(cakes,N,K,done,area,last_rad,now+1));
        }




}


bool fun(pair<double,double> p1, pair<double,double>p2){
    if(p2.first>p1.first){
        return false;
    }else if(p2.first==p1.first){
        if(p2.second>p1.second){
            return false;
        }else{
            return true;
        }

    }else{
        return true;
    }
}

int main()
{
  ifstream infile;
  ofstream outfile;
  infile.open ("small_input.txt");
  outfile.open("small_output.txt");
  string s;
  int T;
  //getline(infile,s);
  infile>>T;
  for(int i=1;i<=T;i++)
  {

    int N,K;
    infile>>N>>K;
    vector< pair< double, double> > cakes;
    for(int j=0;j<N;j++){
        int rad,he;
        infile>>rad>>he;
        cakes.push_back(make_pair(rad,he));

    }
    sort(cakes.begin(),cakes.end(),fun);


    double ans;
    double max_rad=1000001,marea=0;
    ans=func(cakes,N,K,0,marea,max_rad,0);
    // use mapBPM for bipartite matching and apsp vor floyyd warshall
    outfile<<fixed;
    cout<<fixed;
    outfile<<setprecision(7)<<"Case #"<<i<<": "<<ans<<endl;
    cout<<setprecision(7)<<"Case #"<<i<<": "<<ans<<endl;


  }

  //cout<<s;
  //outfile<<s;
  infile.close();
  outfile.close();
return 0;
}
