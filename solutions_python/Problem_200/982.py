t = int(raw_input())

#
# function getUntidyIndex(s) {
#   // const s = n + '';
#   // let prev = -1;
#   // for (let i = s.length; i >= 1; i -= 1) {
#   //   const r = Math.pow(10, i);
#   //   const x = parseInt(n / r);
#   //   console.log(prev, x);
#   //   if (prev > x) {
#   //     return false;
#   //   }
#   //   prev = x;
#   // }
#   // return true;
#   let p = -1;
#   return s.split('').findIndex((c) => {
#     let result = (p > +c);
#     p = +c;
#     return result;
#   });
# }
#
# function calc(s) {
#   let ss = s+'';
#   for (let i; ~i; i = getUntidyIndex(ss)) {
#     const aa = ss.split('');
#     aa[i - 1] = (+aa[i - 1] - 1)+'';
#     for (let j = i; j < aa.length; j += 1) {
#       aa[j] = '9';
#     }
#
#     let flag = false;
#     ss = aa.filter((a) => {
#       if (a !== '0') {
#         flag = true;
#       }
#       if (!flag) return false;
#       flag = true;
#       return true;
#     }).join('');
#   }
#   return ss;
# }

def solve(s):
    a = list(s)
    while True:
        i = 1
        while i < len(a):
            if int(a[i - 1]) > int(a[i]):
                a[i - 1] = str(int(a[i - 1]) - 1)
                for j in range(i, len(a)):
                    a[j] = '9'
                break
            i += 1
        if i >= len(a):
            break
    return ''.join(a).lstrip('0')

for i in range(1, t + 1):
    n = raw_input()
    print('Case #{}: {}'.format(i, solve(n)))
