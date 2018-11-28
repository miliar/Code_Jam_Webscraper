#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <limits>
#include <iomanip>

using namespace std;

double inf = std::numeric_limits<double>::infinity();


struct horse
{
    double x;
    double v;

    bool operator < (const horse& str) const
    {
        return (x < str.x);
    }
};

void sort(vector<horse> &h)
{
    sort(h.begin(),h.end());
}

double t_coll(horse h1, horse h2)
{
    //if(h1.v == h2.v)
    //    return -1;
    //else
    double t = (h2.x-h1.x)/(h1.v-h2.v);
    if(isnan(t) || t<0)
        return inf;
    else
        return t;
}

double collide(horse &h1, horse &h2)
{



}

double find_next_coll(vector<horse> &horses, double &t_tot)
{
    sort(horses);
    double t_next = inf;
    vector <int> i_next(1);
    for(int i = horses.size()-1; i>=1; --i)
    {
        double tc = t_coll(horses[i],horses[i-1]);
        printf("i %d t %f\n",i,tc);
        if(abs(tc-t_next)<1e-9)
        {
            i_next.push_back(i-1);
        }
        else if(tc<t_next)
        {
            t_next = tc;
            i_next.clear();
            i_next.push_back(i-1);
        }

    }
    cout << t_next << ": ";
    for(int j=0; j<i_next.size(); ++j)
    {
        cout << i_next[j] << " ";
    }
    cout << endl;

    vector<bool> colliding (horses.size(),0);
    for(int i=0; i<i_next.size(); ++i)
    {
        colliding[i_next[i]]=1;
    }
    cout << "colliding" << ": ";
    for(int j=0; j<colliding.size(); ++j)
    {
        cout << colliding[j] << " ";
    }
    cout << endl;

    if(t_next<inf)
    {
        for(int i=0; i<horses.size(); ++i)
        {
            horses[i].x += horses[i].v * t_next;
            if(colliding[i])
                horses[i].v = horses[i+1].v;
        }
        t_tot += t_next;
    }
    return t_next;
}

double test_case(int D, vector<horse> horses)
{
    cout << "-----------" << endl;
    double t_tot = 0;

    do
    {
        cout << "t  " << t_tot << endl;
        for(int i=0; i<horses.size(); ++i)
            cout << setprecision(17) << horses[i].x << "\t";
        cout << endl;
        for(int i=0; i<horses.size(); ++i)
            cout << horses[i].v << "\t";
        cout << endl;

    }
    while(find_next_coll(horses,t_tot)<inf);

    cout << "t_tot" << t_tot << endl;
    double v_max = double(D)/t_tot;
    cout << "v max " << setprecision(17) << v_max << endl;

    return v_max;
}

int main()
{
    ifstream fin("A-small-attempt1.in");
    ofstream fout("A-small-attempt1.out");
    int n_cases;
    fin >> n_cases;
    for(int h=0; h<n_cases; ++h)
    {
        int D,N;
        fin >> D >> N;
        printf("Case %d %d %d\n",h+1,D,N);
        vector<horse> horses (N);
        for(int i=0; i<N; ++i)
        {
            fin >> horses[i].x >> horses[i].v;
        }

        sort(horses);
        horses.push_back({double(D),0});

        for(int i=0; i<horses.size(); ++i)
        {
            cout << horses[i].x << " " << horses[i].v << endl;
        }

        double max_v = test_case(D,horses);

        fout << "Case #" << h+1 << ": " << setprecision(17) << max_v << endl;
    }
}

