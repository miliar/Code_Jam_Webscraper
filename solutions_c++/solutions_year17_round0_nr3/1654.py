#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <queue>
typedef long long Int;
using namespace std;
class state
{
    vector<Int> inc;
    Int cur_max;
    Int p_cur_max;
public:
    Int M_out,m_out;
    state(Int i)
    {
        inc.push_back(i);
        cur_max=i;
        p_cur_max=0;
    }
    void reduce()
    {
        Int _max=cur_max;
        vector<Int> out;
        for(Int i=0; i<inc.size(); i++)
        {
            if(_max==inc[i])
            {
                _max=_max-1;
                Int a=(_max-_max%2)/2;
                Int b=(_max-_max%2)/2+_max%2;
                out.push_back(a);
                out.push_back(b);
                _max=-1;
            }
            else
            {
                out.push_back(inc[i]);
            }
        }
        inc=out;
        cur_max=inc[0];
        for(Int i=1; i<inc.size(); i++)
            if(cur_max<inc[i])
                cur_max=inc[i];
    }
    void print_v()
    {
        cout<<cur_max<<" | ";
        for(Int i=0; i<inc.size(); i++)
            cout<<inc[i]<<" ";
        cout<<endl;
    }
    void calc_out()
    {
        Int _max=cur_max;
        _max=_max-1;
        Int a=(_max-_max%2)/2;
        Int b=(_max-_max%2)/2+_max%2;
        m_out=a;
        M_out=b;
    }
};
void print_v(const vector<Int>&v)
{
    for(Int i=0; i<v.size(); i++)
        cout<<v[i]<<" ";
    cout<<endl;
}

class pointPair
{
public:
    Int num;
    Int cnt;
    pointPair(Int _num)
    {
        num=_num;
        cnt=1;
    }
    pointPair(Int _num,Int _cnt)
    {
        num=_num;
        cnt=_cnt;
    }
    void add(Int k)
    {
        cnt+=k;
    }
    vector<pointPair> produce()
    {
        vector<pointPair> out;
        Int _max=num;
        _max=_max-1;
        Int a=(_max-_max%2)/2;
        Int b=(_max-_max%2)/2+_max%2;
        if(a==b)
        {
            out.push_back(pointPair(a,2*cnt));
        }
        else
        {
            out.push_back(pointPair(b,cnt));
            out.push_back(pointPair(a,cnt));
        }
        return out;
    }
};
state generate_pointPair(Int N,Int K)
{
    vector<pointPair> vec;
    vec.push_back(pointPair(N));
    std::queue<pointPair> myqueue;
    myqueue.push(pointPair(N));

    for(Int i=0; i<vec.size(); i++)
        cout<<vec[i].num<<" "<<vec[i].cnt<<"\n";
    cout<<"---------\n";

    while(!myqueue.empty())
    {
       /* for(Int i=0; i<vec.size(); i++)
            cout<<vec[i].num<<" "<<vec[i].cnt<<"\n";
        cout<<"---------\n";*/

        pointPair p=myqueue.front();
        for(Int i=0; i<vec.size(); i++)
        {
            if(vec[i].num==p.num)
            {
                p.cnt=vec[i].cnt;
                break;
            }

        }
        myqueue.pop();
        vector<pointPair> v=p.produce();
        for(Int i=0; i<v.size(); i++)
        {
            bool exist=false;
            for(Int j=0; j<vec.size(); j++)
            {
                if(vec[j].num==v[i].num)
                {
                    vec[j].add(v[i].cnt);
                    exist=true;
                    break;
                }
            }
            if(!exist)
            {
                vec.push_back(v[i]);
                myqueue.push(v[i]);
            }

        }

    }
    Int i=0;
    for(i=0; i<vec.size(); i++){
        if(K>vec[i].cnt)
            K-=vec[i].cnt;
        else
            break;
    }
    state S(vec[i].num);
    S.calc_out();
    return S;

}
state solve(Int N,Int K)
{
    state S(N);
    S.print_v();
    for(Int i=0; i<K-1; i++)
    {
        S.reduce();
        S.print_v();
    }
    S.calc_out();
    return S;
}

int main()
{
    ifstream in("C-large(1).in");
    ofstream out("A-small.out");
#define cin in
#define cout out
    Int T;
    cin>>T;
    for(Int iT=0; iT<T; iT++)
    {
        Int n,k;
        cin>>n>>k;
        state o=generate_pointPair(n,k);//=solve(n,k);

        cout<<"Case #"<<iT+1<<": ";
        cout<<o.M_out<<" "<<o.m_out<<endl;
    }
    return 0;
    return 0;
}
