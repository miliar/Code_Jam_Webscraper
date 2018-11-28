#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define NL '\n'
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%I64d",&x)
#define sd(x) scanf("%lf",&x)
#define ss(x) scanf("%s",x)
#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define REV(i,j,k) for(i=j;i>=k;i--)
#define READ(f) freopen(f,"r",stdin)
#define WRITE(f) freopen(f,"w",stdout)
#define cnd tree[idx]
#define lnd tree[idx*2]
#define rnd tree[(idx*2)+1]
#define lndp (idx*2),(b),((b+e)/2)
#define rndp (idx*2+1),((b+e)/2+1),(e)
#define pi 2.0*acos(0.0)
#define MOD 1000000007
#define MAX 1450

int a[MAX], N = 1440;
int jack, cam, key;

vector < pii > vec;

void process_11(int idx, int pr)
{
    if(idx >= N)
        return ;
    if(pr == key && a[idx] == 0)
    {
        int cnt = 0;
        for(int i = idx; i < N; i++)
        {
            if(a[i] == key)
            {
                vec.pb( mp(cnt, idx) );
                process_11(i+1, a[i]);
                return ;
            }
            else if(a[i] != 0)
            {
                process_11(i+1, a[i]);
                return ;
            }
            cnt++;
        }
    }
    else process_11(idx+1, a[idx]);
}

void fill_first()
{
    for(int i = 0; i < N; i++)
    {
        if(a[i] != 0 && a[i] != key) return ;
        if(a[i] == key)
        {
            if(i <= cam)
            {
                for(int j = 0; j < i; j++)
                    a[j] = key;
                cam -= i;
            }
            return ;
        }
    }
}

void fill_last()
{
    for(int i = N-1; i >= 0; i--)
    {
        if(a[i] != 0 && a[i] != key) return ;
        if(a[i] == key)
        {
            if(N-i-1 <= cam)
            {
                for(int j = i+1; j < N; j++)
                    a[j] = key;
                cam -= (N-i-1);
            }
            return ;
        }
    }
}

void go()
{
    cam = 720;
    int i;

    FOR(i,0,N-1)
    {
        if(a[i] == key)
            cam--;
    }

    sort(vec.begin(), vec.end());

    for(int i = 0; i < vec.size(); i++)
    {
        if(cam >= vec[i].xx)
        {
            if(vec[i].yy == -1)
            {
                for(int j = 0; j < N; j++)
                {
                    if(a[i] != 0) break;
                    a[i] = key;
                }
                for(int j = N-1; j >= 0; j--)
                {
                    if(a[i] != 0) break;
                    a[i] = key;
                }
            }
            else
            {
                for(int j = vec[i].yy; j < vec[i].xx+vec[i].yy; j++)
                    a[j] = key;
            }
            cam -= vec[i].xx;
        }
        else break;
        //cout << i << " " << vec[i].xx << " " << vec[i].yy << " " << cam << NL;
    }

    fill_first();
    fill_last();
}

void touched(int key)
{
    if(cam > 0 && a[0] == 0 && a[N-1] == key)
    {
        a[0] = key;
        cam--;
    }
    for(int i = 1; i < N; i++)
    {
        if(cam == 0) return ;
        if(a[i] == 0 && a[i-1] == key)
        {
            a[i] = key;
            cam--;
        }
    }
    if(cam > 0 && a[0] == 0 && a[N-1] == key)
    {
        a[0] = key;
        cam--;
    }
    if(cam > 0 && a[N-1] == 0 && a[0] == key)
    {
        a[N-1] = key;
        cam--;
    }
    for(int i = N-2; i >= 0; i--)
    {
        if(cam == 0) return ;
        if(a[i] == 0 && a[i+1] == key)
        {
            a[i] = key;
            cam--;
        }
    }
    if(cam > 0 && a[N-1] == 0 && a[0] == key)
    {
        a[N-1] = key;
        cam--;
    }
}

void khali(int key)
{
    for(int i = 0; i < N; i++)
    {
        if(cam == 0) return ;
        if(a[i] == 0)
        {
            a[i] = key;
            cam--;
        }
    }
}

void solve()
{
    cam = jack = 720;
    int i;

    FOR(i,0,N-1)
    {
        if(a[i] == 1)
            cam--;
        else if(a[i] == 2)
            jack--;
    }

    touched(1);
    swap(cam, jack);
    touched(2);
    swap(cam, jack);
    khali(1);
    swap(cam, jack);
    khali(2);
}

int ff()
{
    int ret = 0, pr = a[N-1];
    for(int i = 0; i < N; i++)
    {
        if(pr != a[i]) ret++;
        pr = a[i];
    }
    //cout << a[0] << " " << a[N-1] << NL;
    return ret;
}

void extra()
{
    int f = -1;
    for(int i = 0; i < N; i++)
    {
        if(a[i] == key)
        {
            f = i;
            break;
        }
        else if(a[i] != 0) return ;
    }
    if(f == -1) return ;
    for(int i = N-1; i >= 0; i--)
    {
        if(a[i] == key)
        {
            vec.pb( mp(f+N-i-1,-1) );
            return ;
        }
        else if(a[i] != 0) return ;
    }
}

int main()
{
    //READ("B-large.in");
    //WRITE("B-large.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, n, i, j, k, x, y;

    cin >> cases;

    while(cases--)
    {
        cin >> cam >> jack;

        mem(a,0);
        /*
        if(cam == 0 && jack == 0)
        {
            cout << "Case #" << ++caseno << ": " << 2 << NL;
            continue;
        }*/
        if(jack == 0) swap(cam, jack);

        FOR(i,1,cam)
        {
            cin >> x >> y;
            while(x < y)
            {
                a[x] = 2;
                x++;
            }
        }

        FOR(i,1,jack)
        {
            cin >> x >> y;
            while(x < y)
            {
                a[x] = 1;
                x++;
            }
        }

        key = 1;
        vec.clear();
        //extra();
        process_11(0,0);
        go();

        key = 2;
        vec.clear();
        //extra();
        process_11(0,0);
        go();

        solve();

        cout << "Case #" << ++caseno << ": " << ff() << NL;
    }

    return 0;
}


