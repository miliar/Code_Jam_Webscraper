#include <iostream>

using namespace std;

struct Tree 
{
    Tree(int _w) : w(_w) { }
    ~Tree()
    {
        delete l;
        delete r;
    }
    int takeASeat()
    {
        if (o) {
            if (l->w >= r->w) {
                return w = max(l->takeASeat(), r->w);
            } else {
                return w = max(l->w, r->takeASeat());
            }
        } else {
            l = new Tree((w-1)/2);
            r = new Tree(w/2);
            o = true;
            w = max(l->w, r->w);
            return w;
        }
    }
    bool o = false;
    int w;
    Tree* l = NULL;
    Tree* r = NULL;
};

int main()
{
    int T;
    cin >> T;
    int N,K;
    for (int caseNum=0; caseNum<T; caseNum++) {
        cin >> N >> K;
        Tree root(N);
        for (int i=0; i<K-1; i++) {
            root.takeASeat();
        }
        int hi = max((root.w-1)/2, root.w/2);
        int lo = min((root.w-1)/2, root.w/2);
        cout << "Case #" << caseNum+1 << ": " << hi << " " << lo << endl;
    }
}
