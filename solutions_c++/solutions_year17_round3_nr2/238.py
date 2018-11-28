#include <bits/stdc++.h>
using namespace std;

struct Elem {
    int f, t;
    void be(int u) {
        cin>>f>>t;
        d=u;
    }
    int d;
};

bool kisebb(Elem a, Elem b) {
    return a.f<b.f;
}

int main()
{
	freopen("be.txt","r",stdin);
	freopen("ki.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc=0;tc<t;tc++) {
        int a, b;
        cin>>a>>b;
        vector<Elem> tab(a+b);
        int atim=720;
        int btim=720;
        for(int i=0;i<a;i++) {
            tab[i].be(0);
            btim-=tab[i].t;
            btim+=tab[i].f;
        }
        for(int i=a;i<a+b;i++) {
            tab[i].be(1);
            atim-=tab[i].t;
            atim+=tab[i].f;
        }
        swap(atim,btim);
        sort(tab.begin(),tab.end(),kisebb);
        Elem elso=tab[0];
        elso.f+=1440;
        tab.push_back(elso);
        int sol=0;
        vector<int> Anak;
        vector<int> Bnek;
        for(int i=0;i<a+b;i++) {
            if(tab[i].d!=tab[i+1].d) {
                sol++;
            }
            else if(tab[i].d==0) {
                Anak.push_back(tab[i+1].f-tab[i].t);
            }
            else {
                Bnek.push_back(tab[i+1].f-tab[i].t);
            }
        }
        sort(Anak.begin(),Anak.end());
        sort(Bnek.begin(),Bnek.end());
        int it=0;
        bool jo=true;
        while(atim>=0 && it<Anak.size() && jo) {
            if(atim>=Anak[it]) {
                atim-=Anak[it];
                it++;
            }
            else {
                jo=false;
            }
        }
        sol+=(Anak.size()-it)*2;

        it=0;
        jo=true;
        while(btim>=0 && it<Bnek.size() && jo) {
            if(btim>=Bnek[it]) {
                btim-=Bnek[it];
                it++;
            }
            else {
                jo=false;
            }
        }
        sol+=(Bnek.size()-it)*2;
        cout<<"Case #"<<tc+1<<": "<<sol<<endl;
	}
    return 0;
}
