#include <bits/stdc++.h>
using namespace std;

const int maxn = 1000 + 10;

char str[maxn];

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n,k,cnt = 0;
    scanf("%d",&n);
    for(int ca = 1; ca <= n; ca ++) {
        scanf("%s",str);
        scanf("%d",&k);
        cnt = 0;
        int len = strlen(str);
        for(int i = 0; str[i] != '\0'; i ++) {
            if(str[i] == '+')   continue;
            else {
                int id = i;
                if(i + k - 1 >= len)    {
                    cnt = -1;
                    break;
                }
                for(int j = 0; j < k; j ++) {
                    if(str[i + j] == '+')   str[i + j] = '-';
                    else                    str[i + j] = '+';
                    if(str[i + j] == '-' &&  id == -1)  id = i + j;
                }
                cnt ++;
                i = id;
            }
        }
        if(cnt != -1)   printf("Case #%d: %d\n",ca,cnt);
        else            printf("Case #%d: IMPOSSIBLE\n",ca);
    }
    return 0;
}
//#include <bits/stdc++.h>
//using namespace std;
//
//
//struct Node{
//    string s;
//    int cnt;
//};
//
//int judge(Node temp){
//    int l=temp.s.length();
//    for(int i=0;i<l;i++){
//        if(temp.s[i]=='-') return 0;
//    }
//    return 1;
//}
//
//
//int main()
//{
////   freopen("in.txt","r",stdin);
//    freopen("A-small-attempt1.in","r",stdin);
//   freopen("A-small-attempt1.out","w",stdout);
//    int t;
//    scanf("%d",&t);
//    for(int c=1;c<=t;c++){
//        int ans=-1;
//        string s;
//        cin>>s;
//        int k;
//        scanf("%d",&k);
//        Node node;
//        node.s=s;
//        node.cnt=0;
//        set<string>vis;
//        queue<Node>q;
//        q.push(node);
//        vis.insert(s);
//        int l=s.length();
//        while(!q.empty()){
//            Node temp=q.front();
//            q.pop();
//            if(judge(temp)==1){
//                ans=temp.cnt;
//                break;
//            }
//            for(int i=0;i+k<=l;i++){
//                Node xia=temp;
//                for(int j=i;j<i+k;j++){
//                    xia.s[j]=(temp.s[j]=='+'?'-':'+');
//                }
//                xia.cnt++;
//                if(vis.find(xia.s)==vis.end()){
//                    vis.insert(xia.s);
//                    q.push(xia);
//                }
//            }
//        }
//        if(ans==-1){
//            printf("Case #%d: IMPOSSIBLE\n",c,ans);
//        }
//        else
//            printf("Case #%d: %d\n",c,ans);
//        while(!q.empty()){
//            q.pop();
//        }
//    }
//
//    return 0;
//}
