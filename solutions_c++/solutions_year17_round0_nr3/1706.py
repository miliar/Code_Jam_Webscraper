#include <bits/stdc++.h>

#define vi vector<int>
#define vb vector<bool>
#define ii pair<long long int, long long int>

using namespace std;

vector<vi> graph;

void printVec(vi a);
void printVec(vector<bool> a);
void printArr(int a[], int n);
void printArr(bool a[], int n);
ii eqldivide(long long int n);
long long int logfn(long long int n);

int main()
{
    int t,m;
    cin >> t;
    for(m=1;m<=t;m++)
    {
        long long int n,k,i;
        cin >> n >> k;
        long long int nppl = logfn(k);
        long long int ngroups = nppl + 1;
        long long int sgrpsize = (n-nppl)/ngroups;
        long long int lgrp = (n-nppl)%ngroups;
        ii ans;
        if(k-nppl <= lgrp)
            ans = eqldivide(sgrpsize+1);
        else
            ans = eqldivide(sgrpsize);
        cout << "Case #" << m << ": ";
        cout << ans.second << " " << ans.first << endl;
    }
    return 0;
}

ii eqldivide(long long int n)
{
    if(n==0)
        return make_pair(0,0);
    if(n%2)
        return make_pair((n-1)/2, (n-1)/2);
    return make_pair((n-1)/2, n/2);
}

long long int logfn(long long int n)
{
    long long int i = 1;
    while(1)
    {
        if(n<2*i)
            return i-1;
        i = 2*i;
    }
    return 0;
}

void printVec(vi a)
{
    vi::iterator it;
    for(it=a.begin();it!=a.end();it++)
        cout << *it << " ";
    cout << endl;
}

void printVec(vector<bool> a)
{
    vector<bool>::iterator it;
    for(it=a.begin();it!=a.end();it++)
        cout << *it << " ";
    cout << endl;
}

void printArr(int a[], int n)
{
    int i;
    for(i=1;i<n;i++)
        cout << a[i] << " ";
    cout << endl;
}

void printArr(bool a[], int n)
{
    int i;
    for(i=1;i<n;i++)
        cout << a[i] << " ";
    cout << endl;
}


