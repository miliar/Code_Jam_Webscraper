//Author: Artem Romanov
#include <bits/stdc++.h>
//#define TASK "file"

/// Algorithms and data structures.
namespace algo {
  /// Global typedef.
  typedef long double dbl;

  using std::swap;

  //@{
  /// Global constant.
  const dbl PI = 3.141592653589793238462643383279502884L;
  const dbl E = 2.718281828459045235360287471352662498L;
  const dbl EPS = 1e-12L;
  //@}

  /**
   * @defgroup math Math
   * Mathematical data structures and algorithms.
   * @{
   *    @defgroup number_theory Number theory
   *    Number theory.
   *    @{
   *        @defgroup modular Modular arithmetic
   *        Modular arithmetic operations.
   *    @}
   * @}
   */

  /// @addtogroup math
  /// @{

  /**
   * @brief Binary exponentiation.
   * @param a The base.
   * @param n The exponent.
   * @return @a a raised to the power @a n.
   *
   * Calculates <i>n</i>-th power of @a a.
   *
   * @b Complexity: @f$O(\log n)@f$
   */
  template<typename T1, typename T2>
  T1 bin_pow(T1 a, T2 n) {
    T1 r{1};
    while (n > 0) {
      if (n % 2 == 1)
        r *= a;
      a *= a;
      n /= 2;
    }
    return r;
  }

  /**
   * @brief Modular exponentiation.
   * @param a The base.
   * @param n The exponent.
   * @param m The modulus.
   * @return @a a raised to the power @a n modulo @a m.
   *
   * Calculates <i>n</i>-th power of @a a modulo @a m.
   *
   * @b Complexity: @f$O(\log n)@f$
   */
  template<typename T1, typename T2>
  T1 bin_pow(T1 a, T2 n, const T1& m) {
    if (m == 1)
      return 0;
    T1 r{1};
    while (n > 0) {
      if (n % 2 == 1) {
        r *= a;
        r %= m;
      }
      a *= a;
      a %= m;
      n /= 2;
    }
    return r;
  }

  /**
   * @brief Number to Roman numeral conversion.
   * @param n The number.
   * @return @a string containing the Roman numeral representation of number.
   *
   * Converts number into Roman numeral.
   *
   * @b Complexity: @f$O(1)@f$
   */
  std::string to_roman(int n) {
    static std::string d[3][10] = {
        {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"},
        {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"},
        {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}
    };
    std::string res(n / 1000U, 'M');
    n %= 1000;
    return res + d[0][n / 100] + d[1][n / 10 % 10] + d[2][n % 10];
  }

  /**
   * @brief Roman numeral to number conversion.
   * @param n Roman numeral.
   * @return the number.
   *
   * Converts Roman numeral into number.
   *
   * @b Complexity: @f$O(1)@f$
   */
  int from_roman(const std::string& n) {
    auto to_int = [](char c) -> int {
      switch (c) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;
      }
    };

    int r = 0, p = 0;
    for (auto it = n.rbegin(); it != n.rend(); ++it) {
      int inc = to_int(*it);
      r += inc < p ? -inc : inc;
      p = inc;
    }
    return r;
  }

  /// @} math

  /// @addtogroup number_theory
  /// @{

  /**
   * @brief Euclid's algorithm.
   * @param a,b The numbers.
   * @return greatest common divisor of @a a and @a b.
   *
   * Calculates greatest common divisor of @a a and @a b.
   *
   * @b Complexity: @f$O(\log \min(a,b))@f$
   */
  template<typename T>
  T gcd(const T& a, const T& b) {
    if (b == 0)
      return a < 0 ? -a : a;
    return gcd(b, a % b);
  }

  /**
   * @brief Extended Euclidean algorithm.
   * @param a,b The numbers.
   * @param x,y The coefficients.
   * @return greatest common divisor of @a a and @a b.
   *
   * Calculates greatest common divisor of @a a and @a b and the coefficients
   * (@a x and @a y) such that @f$ax+by=\gcd(a,b)@f$.
   *
   * @b Complexity: @f$O(\log \min(a,b))@f$
   */
  template<typename T>
  T gcd(const T& a, const T& b, T& x, T& y) {
    if (b == 0) {
      x = a < 0 ? -1 : 1;
      y = 0;
      return x * a;
    }
    T d{gcd(b, a % b, y, x)};
    y -= (a / b) * x;
    return d;
  }

  /**
   * @brief Least common multiple.
   * @param a,b The numbers.
   * @return least common multiple of @a a and @a b.
   *
   * Calculates least common multiple of @a a and @a b.
   *
   * @b Complexity: @f$O(\log \min(a,b))@f$
   */
  template<typename T>
  T lcm(const T& a, const T& b) {
    T r{a / gcd(a, b) * b};
    return r < 0 ? -r : r;
  }

  /// @addtogroup modular
  /// @{

  /**
   * @brief Modular addition.
   * @param a,b The numbers.
   * @param m The modulus.
   * @return @a a + @a b modulo @a m.
   *
   * Calculates sum of @a a and @a b modulo @a m.
   *
   * @b Complexity: @f$O(1)@f$
   */
  template<typename T>
  T mod_add(const T& a, const T& b, const T& m) {
    if (a < m - b)
      return a + b;
    return a - (m - b);
  }

  /**
   * @brief Modular subtraction.
   * @param a,b The numbers.
   * @param m The modulus.
   * @return @a a - @a b modulo @a m.
   *
   * Calculates difference between @a a and @a b modulo @a m.
   *
   * @b Complexity: @f$O(1)@f$
   */
  template<typename T>
  T mod_sub(const T& a, const T& b, const T& m) {
    if (a < b)
      return a + (m - b);
    return a - b;
  }

  /**
   * @brief Modular multiplication.
   * @param a,b The numbers.
   * @param m The modulus.
   * @return @a a × @a b modulo @a m.
   *
   * Calculates product of @a a and @a b modulo @a m.
   *
   * @b Complexity: @f$O(\log \min(a,b))@f$
   */
  template<typename T>
  T mod_mul(T a, T b, const T& m) {
    if (b > a)
      swap(a, b);
    T r{0};
    while (b > 0) {
      if (b % 2 == 1)
        r = mod_add(r, a, m);
      a = mod_add(a, a, m);
      b /= 2;
    }
    return r;
  }

  /**
   * @brief Modular exponentiation.
   * @param a The base.
   * @param n The exponent.
   * @param m The modulus.
   * @return @a a raised to the power @a n modulo @a m.
   *
   * Calculates <i>n</i>-th power of @a a modulo @a m.
   *
   * @b Complexity: @f$O(\log a \cdot \log n)@f$
   */
  template<typename T1, typename T2>
  T1 mod_pow(T1 a, T2 n, const T1& m) {
    if (m == 1)
      return 0;
    T1 r{1};
    while (n > 0) {
      if (n % 2 == 1)
        r = mod_mul(r, a, m);
      a = mod_mul(a, a, m);
      n /= 2;
    }
    return r;
  }

  /**
   * @brief Modular multiplicative inverse.
   * @param a The number.
   * @param m The modulus.
   * @return modular multiplicative inverse of @a a if exist, 0 otherwise.
   *
   * Calculates modular multiplicative inverse of @a a under modulo @a m.
   *
   * @b Complexity: @f$O(\log \min(a,m))@f$
   */
  template<typename T>
  T mod_inv(const T& a, const T& m) {
    T x, y;
    T d{gcd(a, m, x, y)};
    if (d != 1)
      return 0;
    if (x < 0)
      x += m;
    return x;
  }

  /**
   * @brief Modular multiplicative inverses of numbers.
   * @param m The modulus.
   * @return @a vector of modular multiplicative inverses under modulo @a m.
   *
   * Calculates modular multiplicative inverse if exist of every number in range
   * @f$[1,m-1]@f$.
   *
   * @b Complexity: @f$O(m)@f$
   */
  std::vector<int32_t> gen_inv(int32_t m) {
    std::vector<int32_t> r(static_cast<size_t>(m));
    if (m > 1) {
      r[1] = 1;
      for (int i = 2; i < m; ++i)
        r[i] = (m - static_cast<int32_t>((m / i) * 1LL * r[m % i] % m)) % m;
    }
    return r;
  }

  /// @} modular

  /// @addtogroup math
  /// @{

  /**
   * @brief Unsigned 64-bit integer multiplication.
   * @param a,b The numbers.
   * @param lo,hi lower and higher 64-bit parts of @a a × @a b.
   *
   * Calculates lower and higher 64-bit parts of product of @a a and @a b.
   *
   * @b Complexity: @f$O(1)@f$
   */
  void mul_u128(uint64_t a, uint64_t b, uint64_t& lo, uint64_t& hi) {
#ifndef __x86_64__
    uint64_t a_hi = a >> 32;
    uint64_t a_lo = a & 0xffffffffULL;
    uint64_t b_hi = b >> 32;
    uint64_t b_lo = b & 0xffffffffULL;
    uint64_t a_hi_b_hi = a_hi * b_hi;
    uint64_t a_hi_b_lo = a_hi * b_lo;
    uint64_t a_lo_b_hi = a_lo * b_hi;
    uint64_t a_lo_b_lo = a_lo * b_lo;
    uint64_t middle = a_hi_b_lo + a_lo_b_hi;
    hi = a_hi_b_hi + (middle >> 32);
    lo = a_lo_b_lo + (middle << 32);
    if (middle < a_hi_b_lo)
      hi += 1ULL << 32;
    hi += lo < a_lo_b_lo;
#else
    asm("mulq %3" : "=a"(lo), "=d"(hi) : "a"(a), "rm"(b));
#endif
  };

  /**
   * @brief Modular unsigned 64-bit integer multiplication.
   * @param a,b The numbers.
   * @param m The modulus.
   * @return @a a × @a b modulo @a m.
   *
   * Calculates product of unsigned 64-bit integers @a a and @a b modulo @a m.
   *
   * @b Complexity: Architecture dependent @f$O(1)@f$ or @f$O(\log \min(a,b))@f$
   */
  uint64_t mul_mod_u64(uint64_t a, uint64_t b, uint64_t m) {
    if (a >= m)
      a %= m;
    if (b >= m)
      b %= m;
#ifndef __x86_64__
    if ((a | b) < 1ULL << 32)
      return (a * b) % m;
    uint64_t r = mod_mul(a, b, m);
#else
    uint64_t r, u;
    asm("mulq %3\n\tdivq %4":"=a"(u), "=&d"(r):"a"(a), "rm"(b), "rm"(m):"cc");
#endif
    return r;
  }

  /// @} math

  /**
   * @brief Euler's totient function.
   * @param n The number.
   * @return @f$\varphi(n)@f$, Euler's totient function of @a n.
   *
   * Calculates number of positive integers up to @a n that are relatively
   * prime to @a n.
   *
   * @b Complexity: @f$O(\sqrt n)@f$
   */
  template<typename T>
  T phi(T n) {
    T t = std::sqrt(n) + EPS;
    T r = n;
    for (T i = 2; i <= t; ++i) {
      if (n % i == 0) {
        r -= r / i;
        do {
          n /= i;
        } while (n % i == 0);
        t = std::sqrt(n) + EPS;
      }
    }
    if (n > 1)
      r -= r / n;
    return r;
  }

  /**
   * @brief Linear Euler's totient function.
   *
   * Calculates Euler's totient function for all numbers on interval
   * @f$[1;n]@f$.
   *
   * @b Memory @b usage:
   * @f$(4+\frac{1}{8})\cdot\frac{n}{2}+4\cdot\frac{n}{\log n}@f$ bytes
   */
  class LinearPhi {
   public:
    //@{
    /// Public typedef.
    typedef int32_t value_type;
    typedef uint32_t size_type;
    //@}

    /**
     * @brief Creates a @a LinearPhi.
     * @param n Size of @a LinearPhi.
     *
     * Builds @a LinearPhi for numbers on interval @f$[1;n]@f$.
     *
     * @b Complexity: @f$O(n)@f$
     */
    LinearPhi(size_type n = 1 << 20) : size_{n} {
      assert(size_ > 0 && "Size should be nonzero");
      assert(size_ <= INT32_MAX && "Size should fit into an 32-bit signed int");
      size_type sz = (size_ + 1) / 2;
      phi_ = new value_type[sz];
      mark_.assign(sz, false);
      phi_[0] = 1;
      if (size_ > 1)
        primes_.push_back(2);
      for (size_type i = 1; i < sz; ++i) {
        size_type val = i << 1 | 1;
        if (!mark_[i]) {
          phi_[i] = val - 1;
          primes_.push_back(val);
        }
        if (val < sz) {
          for (size_type j = 1; j < primes_.size(); ++j) {
            size_type t = val * primes_[j];
            if (t > size_)
              break;
            mark_[t >> 1] = true;
            if (val % primes_[j] == 0) {
              phi_[t >> 1] = phi_[i] * primes_[j];
              break;
            }
            phi_[t >> 1] = phi_[i] * (primes_[j] - 1);
          }
        }
      }
    }

    LinearPhi(const LinearPhi&) = delete;
    LinearPhi& operator=(const LinearPhi&) = delete;

    /// The @a LinearPhi destructor.
    ~LinearPhi() {
      delete[] phi_;
      phi_ = nullptr;
    }

    /**
     * @brief Size of @a LinearPhi.
     * @return size of @a LinearPhi.
     *
     * Returns size of @a LinearPhi.
     *
     * @b Complexity: @f$O(1)@f$
     */
    const size_type& size() const {
      return size_;
    }

    //@{
    /**
     * @brief Euler's totient function.
     * @param i The number.
     * @return @f$\varphi(i)@f$, Euler's totient function of @a i.
     *
     * Calculates number of positive integers up to @a i that are relatively
     * prime to @a i.
     *
     * @b Complexity: @f$O(1)@f$
     */
    value_type phi(value_type i) const {
      value_type r = 1;
      int k = __builtin_ctz(i);
      if (k > 0) {
        i >>= k;
        r <<= k - 1;
      }
      return r * phi_[i >> 1];
    }

    value_type operator[](value_type i) const {
      return phi(i);
    }
    //@}

    /**
     * @brief Prime numbers.
     * @return @a vector of prime numbers on interval @f$[1;size]@f$.
     *
     * Prime numbers on interval @f$[1;size]@f$.
     *
     * @b Complexity: @f$O(1)@f$
     */
    const std::vector<value_type>& primes() const {
      return primes_;
    }

   private:
    value_type* phi_ = nullptr;
    std::vector<bool> mark_;
    size_type size_;
    std::vector<value_type> primes_;
  };

  /**
   * @brief Sieve of Eratosthenes.
   *
   * Finds all prime numbers on interval @f$[1;n]@f$.
   *
   * For @f$n>2\cdot 10^{8}@f$ use @a algo::isPrime().
   *
   * @b Memory @b usage: @f$\frac{1}{8}\cdot\frac{n}{2}@f$ bytes
   */
  class Sieve {
   public:
    //@{
    /// Public typedef.
    typedef int32_t value_type;
    typedef uint32_t size_type;
    //@}

    /**
     * @brief Creates a @a Sieve.
     * @param n Size of sieve.
     *
     * Builds @a Sieve for numbers on interval @f$[1;n]@f$.
     *
     * @b Complexity: @f$O(n \log \log n)@f$
     */
    Sieve(size_type n = 1 << 20) : size_{n} {
      assert(size_ > 0 && "Size should be nonzero");
      assert(size_ <= INT32_MAX && "Size should fit into an 32-bit signed int");
      size_type sz = (size_ + 1) / 2;
      prime_.assign(sz, true);
      prime_[0] = false;
      for (size_type i = 1; i < sz; ++i) {
        size_type val = i << 1 | 1;
        if (prime_[i] && val * 1ULL * val <= size_)
          for (size_type j = val * val; j <= size_; j += 2 * val)
            prime_[j >> 1] = false;
      }
    }

    Sieve(const Sieve&) = delete;
    Sieve& operator=(const Sieve&) = delete;

    /**
     * @brief Size of sieve.
     * @return size of sieve.
     *
     * Returns size of @a Sieve.
     *
     * @b Complexity: @f$O(1)@f$
     */
    const size_type& size() const {
      return size_;
    }

    //@{
    /**
     * @brief Check if number is prime.
     * @param i The number.
     * @return @a true if @a i is prime, @a false otherwise.
     *
     * Checks if @a i is a prime number.
     *
     * @b Complexity: @f$O(1)@f$
     */
    bool isPrime(const value_type& i) const {
      if (i % 2 == 0)
        return i == 2;
      return prime_[i >> 1];
    }

    bool operator[](const value_type& i) const {
      return isPrime(i);
    }
    //@}

   private:
    size_type size_;
    std::vector<bool> prime_;
  };

  /**
   * @brief Linear sieve of Eratosthenes.
   *
   * Calculates factorization and finds all prime numbers on interval
   * @f$[1;n]@f$.
   *
   * @b Memory @b usage: @f$2\cdot\frac{n}{2}+4\cdot\frac{n}{\log n}@f$ bytes
   */
  class LinearSieve {
   public:
    //@{
    /// Public typedef.
    typedef int32_t value_type;
    typedef uint32_t size_type;
    //@}

    /**
     * @brief Creates a @a LinearSieve.
     * @param n Size of sieve.
     *
     * Builds @a LinearSieve for numbers on interval @f$[1;n]@f$.
     *
     * @b Complexity: @f$O(n)@f$
     */
    LinearSieve(size_type n = 1 << 20) : size_{n} {
      assert(size_ > 0 && "Size should be nonzero");
      assert(size_ <= INT32_MAX && "Size should fit into an 32-bit signed int");
      size_type sz = (size_ + 1) / 2;
      lpf_ = new uint16_t[sz];
      std::fill(lpf_, lpf_ + sz, 0);
      lpf_[0] = 1;
      if (size_ > 1)
        primes_.push_back(2);
      for (size_type i = 1; i < sz; ++i) {
        size_type val = i << 1 | 1;
        if (!lpf_[i])
          primes_.push_back(val);
        if (val < sz) {
          for (size_type j = 1; j < primes_.size(); ++j) {
            size_type t = val * primes_[j];
            if (t > size_)
              break;
            lpf_[t >> 1] = static_cast<uint16_t>(primes_[j]);
            if (lpf_[t >> 1] == (lpf_[i] ? lpf_[i] : val))
              break;
          }
        }
      }
    }

    LinearSieve(const LinearSieve&) = delete;
    LinearSieve& operator=(const LinearSieve&) = delete;

    /// The @a LinearSieve destructor.
    ~LinearSieve() {
      delete[] lpf_;
      lpf_ = nullptr;
    }

    /**
     * @brief Size of sieve.
     * @return size of sieve.
     *
     * Returns size of @a LinearSieve.
     *
     * @b Complexity: @f$O(1)@f$
     */
    const size_type& size() const {
      return size_;
    }

    //@{
    /**
     * @brief Check if number is prime.
     * @param i The number.
     * @return @a true if @a i is prime, @a false otherwise.
     *
     * Checks if @a i is a prime number.
     *
     * @b Complexity: @f$O(1)@f$
     */
    bool isPrime(const value_type& i) const {
      if (i % 2 == 0)
        return i == 2;
      return !lpf_[i >> 1];
    }

    bool operator[](const value_type& i) const {
      return isPrime(i);
    }
    //@}

    /**
     * @brief Least prime factor.
     * @param i The number.
     * @return least prime factor of @a i.
     *
     * Calculates least prime factor of @a i.
     *
     * @b Complexity: @f$O(1)@f$
     */
    value_type lpf(const value_type& i) const {
      if (i % 2 == 0)
        return 2;
      if (!lpf_[i >> 1])
        return i;
      return lpf_[i >> 1];
    }

    /**
     * @brief Euler's totient function.
     * @param i The number.
     * @return @f$\varphi(i)@f$, Euler's totient function of @a i.
     *
     * Calculates number of positive integers up to @a i that are relatively
     * prime to @a i.
     *
     * @b Complexity: @f$O(\log \log n)@f$
     */
    value_type phi(value_type i) const {
      value_type r = 1;
      int k = __builtin_ctz(i);
      if (k > 0) {
        i >>= k;
        r <<= k - 1;
      }
      value_type n, t = lpf_[i >> 1] ? lpf_[i >> 1] : i;
      while (t != 1) {
        r *= (t - 1);
        i /= t;
        n = lpf_[i >> 1] ? lpf_[i >> 1] : i;
        while (n == t) {
          r *= n;
          i /= t;
          n = lpf_[i >> 1] ? lpf_[i >> 1] : i;
        }
        t = n;
      }
      return r;
    }

    /**
     * @brief Prime numbers.
     * @return @a vector of prime numbers on interval @f$[1;size]@f$.
     *
     * Prime numbers on interval @f$[1;size]@f$.
     *
     * @b Complexity: @f$O(1)@f$
     */
    const std::vector<value_type>& primes() const {
      return primes_;
    }

   private:
    uint16_t* lpf_ = nullptr;
    size_type size_;
    std::vector<value_type> primes_;
  };

  /**
   * @brief Strong probable-prime checker.
   * @param n The number.
   * @param a The base.
   * @return @a true if @a n is an <i>a</i>-SPRP, @a false otherwise.
   *
   * Checks if @a n is a strong probable-prime base @a a (an <i>a</i>-SPRP).
   *
   * @b Complexity: @f$O(\log n)@f$
   */
  bool isSprp(uint32_t n, uint32_t a) {
    uint32_t d = n - 1;
    int s = __builtin_ctz(d);
    d >>= s;
    uint64_t b = a, r = 1;
    while (d > 0) {
      if (d & 1)
        r = (r * b) % n;
      b = (b * b) % n;
      d >>= 1;
    }
    if (r == 1)
      return true;
    b = n - 1;
    for (int i = 1; i < s; ++i) {
      if (r == b)
        return true;
      r = (r * r) % n;
    }
    return r == b;
  }

  /**
   * @brief Strong probable-prime checker.
   * @param n The number.
   * @param v @a vector of bases.
   * @return @a true if @a n is an <i>v[i]</i>-SPRP, @a false otherwise.
   *
   * Checks if @a n is a strong probable-prime bases @a v.
   *
   * [Montgomery math.]
   * (http://cpansearch.perl.org/src/DANAJ/Math-Prime-Util-0.60/montmath.h)
   *
   * @b Complexity: @f$O(k\log n)@f$, where @a k is number of bases.
   */
  bool isSprp(uint64_t n, const std::vector<uint64_t>& v) {
    // Computes 2^64 mod n
    auto mont_u64_mod_n = [&]() -> uint64_t {
      if (n <= (1ULL << 63)) {
        uint64_t res = ((1ULL << 63) % n) << 1;
        return res < n ? res : res - n;
      }
      return 0ULL - n;
    };

    // Computes -n^-1 mod 2^64
    auto mont_inv = [&]() -> uint64_t {
      uint64_t j, s = 1;
      uint32_t i, t;
      static const uint8_t masks[128] = {
          255, 85, 51, 73, 199, 93, 59, 17, 15, 229, 195, 89, 215, 237, 203, 33,
          31, 117, 83, 105, 231, 125, 91, 49, 47, 5, 227, 121, 247, 13, 235, 65,
          63, 149, 115, 137, 7, 157, 123, 81, 79, 37, 3, 153, 23, 45, 11, 97,
          95, 181, 147, 169, 39, 189, 155, 113, 111, 69, 35, 185, 55, 77, 43,
          129, 127, 213, 179, 201, 71, 221, 187, 145, 143, 101, 67, 217, 87,
          109, 75, 161, 159, 245, 211, 233, 103, 253, 219, 177, 175, 133, 99,
          249, 119, 141, 107, 193, 191, 21, 243, 9, 135, 29, 251, 209, 207, 165,
          131, 25, 151, 173, 139, 225, 223, 53, 19, 41, 167, 61, 27, 241, 239,
          197, 163, 57, 183, 205, 171, 1
      };
      uint8_t mask = masks[(n >> 1) & 127];
      i = (uint32_t) ((mask * (s & 255)) & 255);
      j = i;
      s = (s + n * i) >> 8;
      i = (uint32_t) ((mask * (s & 255)) & 255);
      j |= (uint64_t) i << 8;
      s = (s + n * i) >> 8;
      i = (uint32_t) ((mask * (s & 255)) & 255);
      j |= (uint64_t) i << 16;
      s = (s + n * i) >> 8;
      i = (uint32_t) ((mask * (s & 255)) & 255);
      j |= (uint64_t) i << 24;
      t = (uint32_t) ((s + n * i) >> 8);
      i = (mask * (t & 255)) & 255;
      j |= (uint64_t) i << 32;
      t = (uint32_t) ((t + n * i) >> 8);
      i = (mask * (t & 255)) & 255;
      j |= (uint64_t) i << 40;
      t = (uint32_t) ((t + n * i) >> 8);
      i = (mask * (t & 255)) & 255;
      j |= (uint64_t) i << 48;
      t = (uint32_t) ((t + n * i) >> 8);
      i = (mask * (t & 255)) & 255;
      j |= (uint64_t) i << 56;
      return j;
    };

    // Montgomery modular multiplication
    auto mont_mod_mul = [=](uint64_t a, uint64_t b, uint64_t npi) -> uint64_t {
      uint64_t ab_lo, ab_hi, mn_lo, mn_hi;
      uint64_t m, u;
      int carry;
      mul_u128(a, b, ab_lo, ab_hi);
      m = ab_lo * npi;
      mul_u128(m, n, mn_lo, mn_hi);
      carry = ab_lo + mn_lo < ab_lo ? 1 : 0;
      u = ab_hi + mn_hi + carry;
      return (u < ab_hi || u >= n) ? u - n : u;
    };

    if (n % 2 == 0) return n == 2;
    if (n % 3 == 0) return n == 3;
    if (n % 5 == 0) return n == 5;
    if (n % 7 == 0) return n == 7;
    if (n < 121) return n > 1;
    uint64_t d = n - 1;
    int s = __builtin_ctzll(d);
    d >>= s;
    uint64_t npi = mont_inv();
    uint64_t r = mont_u64_mod_n();
    uint64_t nr = n - r;
    for (uint32_t i = 0; i < v.size(); ++i) {
      uint64_t a = mul_mod_u64(v[i], r, n);
      uint64_t b = r, k = d;
      if (a == 0)
        continue;
      while (k > 0) {
        if (k & 1)
          b = mont_mod_mul(b, a, npi);
        a = mont_mod_mul(a, a, npi);
        k >>= 1;
      }
      if (b == r || b == nr)
        continue;
      int j;
      for (j = 1; j < s; ++j) {
        b = mont_mod_mul(b, b, npi);
        if (b == r)
          return false;
        if (b == nr)
          break;
      }
      if (j == s)
        return false;
    }
    return true;
  }

  //@{
  /**
   * @brief Hash-based Miller–Rabin 32-bit integer primality test.
   * @param n The number.
   * @return @a true if @a n is prime, @a false otherwise.
   *
   * Checks if 32-bit integer @a n is a prime number.
   *
   * [Research.](http://ceur-ws.org/Vol-1326/020-Forisek.pdf)
   *
   * @b Complexity: @f$O(\log n)@f$
   */
  bool isPrime(uint32_t n) {
    static const uint32_t bases[] = {
        0x3ce7, 0x07e2, 0x00a6, 0x1d05, 0x1f80, 0x3ead, 0x2907, 0x112f,
        0x079d, 0x050f, 0x0ad8, 0x0e24, 0x0230, 0x0c38, 0x145c, 0x0a61,
        0x08fc, 0x07e5, 0x122c, 0x05bf, 0x2478, 0x0fb2, 0x095e, 0x4fee,
        0x2825, 0x1f5c, 0x08a5, 0x184b, 0x026c, 0x0eb3, 0x12f4, 0x1394,
        0x0c71, 0x0535, 0x1853, 0x14b2, 0x0432, 0x0957, 0x13f9, 0x1b95,
        0x0323, 0x04f5, 0x0f23, 0x01a6, 0x02ef, 0x0244, 0x1279, 0x27ff,
        0x02ea, 0x0b87, 0x022c, 0x089e, 0x0ec2, 0x01e1, 0x05f2, 0x0d94,
        0x01e1, 0x09b7, 0x0cc2, 0x1601, 0x01e8, 0x0d2d, 0x1929, 0x0d10,
        0x0011, 0x3b01, 0x05d2, 0x103a, 0x07f4, 0x075a, 0x0715, 0x01d3,
        0x0ceb, 0x36da, 0x18e3, 0x0292, 0x03ed, 0x0387, 0x02e1, 0x075f,
        0x1d17, 0x0760, 0x0b20, 0x06f8, 0x1d87, 0x0d48, 0x03b7, 0x3691,
        0x10d0, 0x00b1, 0x0029, 0x4da3, 0x0c26, 0x33a5, 0x2216, 0x023b,
        0x1b83, 0x1b1f, 0x04af, 0x0160, 0x1923, 0x00a5, 0x0491, 0x0cf3,
        0x03d2, 0x00e9, 0x0bbb, 0x0a02, 0x0bb2, 0x295b, 0x272e, 0x0949,
        0x076e, 0x14ea, 0x115f, 0x0613, 0x0107, 0x6993, 0x08eb, 0x0131,
        0x029d, 0x0778, 0x0259, 0x182a, 0x01ad, 0x078a, 0x3a19, 0x06f8,
        0x067d, 0x020c, 0x0df9, 0x00ec, 0x0938, 0x1802, 0x0b22, 0xd955,
        0x06d9, 0x1052, 0x2112, 0x00de, 0x0a13, 0x0ab7, 0x07ef, 0x08b2,
        0x08e4, 0x0176, 0x0854, 0x032d, 0x5cec, 0x064a, 0x1146, 0x1427,
        0x06bd, 0x0e0d, 0x0d26, 0x3800, 0x0243, 0x00a5, 0x055f, 0x2722,
        0x3148, 0x2658, 0x055b, 0x0218, 0x074b, 0x2a70, 0x0359, 0x089e,
        0x169c, 0x01b2, 0x1f95, 0x44d2, 0x02d7, 0x0e37, 0x063b, 0x1350,
        0x0851, 0x07ed, 0x2003, 0x2098, 0x1858, 0x23df, 0x1fbe, 0x074e,
        0x0ce0, 0x1d1f, 0x22f3, 0x61b9, 0x021d, 0x4aab, 0x0170, 0x0236,
        0x162a, 0x019b, 0x020a, 0x0403, 0x2017, 0x0802, 0x1990, 0x2741,
        0x0266, 0x0306, 0x091d, 0x0bbf, 0x8981, 0x1262, 0x0480, 0x06f9,
        0x0404, 0x0604, 0x0e9f, 0x01ed, 0x117a, 0x09d9, 0x68dd, 0x20a2,
        0x0360, 0x49e3, 0x1559, 0x098f, 0x002a, 0x119f, 0x067c, 0x00a6,
        0x04e1, 0x1873, 0x09f9, 0x0130, 0x0110, 0x1c76, 0x0049, 0x199a,
        0x0383, 0x0b00, 0x144d, 0x3412, 0x1b8e, 0x0b02, 0x0c7f, 0x032b,
        0x039a, 0x015e, 0x1d5a, 0x1164, 0x0d79, 0x0a67, 0x1264, 0x01a2,
        0x0655, 0x0493, 0x0d8f, 0x0058, 0x2c51, 0x019c, 0x0617, 0x00c2
    };
    if (n % 2 == 0) return n == 2;
    if (n % 3 == 0) return n == 3;
    if (n % 5 == 0) return n == 5;
    if (n % 7 == 0) return n == 7;
    if (n < 121) return n > 1;
    uint64_t h = n;
    h = ((h >> 16) ^ h) * 0x45d9f3b;
    h = ((h >> 16) ^ h) * 0x45d9f3b;
    h = ((h >> 16) ^ h) & 0xff;
    return isSprp(n, bases[h]);
  }

  bool isPrime(int32_t n) {
    return isPrime(static_cast<uint32_t>(n));
  }
  //@}

  //@{
  /**
   * @brief Miller–Rabin 64-bit integer primality test.
   * @param n The number.
   * @return @a true if @a n is prime, @a false otherwise.
   *
   * Checks if 64-bit integer @a n is a prime number.
   *
   * Count of rounds of testing @a k:
   * - 1. @a n < 4294967296
   * - 3. @a n < 350269456337
   * - 4. @a n < 55245642489451
   * - 5. @a n < 7999252175582851
   * - 6. @a n < 585226005592931977
   * - 7. @a n < 18446744073709551616
   *
   * [Constants.](http://miller-rabin.appspot.com/)
   *
   * @b Complexity: @f$O(k\log n)@f$
   */
  bool isPrime(uint64_t n) {
    static const std::vector<uint64_t> bases[] = {
        {4230279247111683200ULL, 14694767155120705706ULL,
         16641139526367750375ULL},
        {2ULL, 141889084524735ULL, 1199124725622454117ULL,
         11096072698276303650ULL},
        {2ULL, 4130806001517ULL, 149795463772692060ULL, 186635894390467037ULL,
         3967304179347715805ULL},
        {2ULL, 123635709730000ULL, 9233062284813009ULL, 43835965440333360ULL,
         761179012939631437ULL, 1263739024124850375ULL},
        {2ULL, 325ULL, 9375ULL, 28178ULL, 450775ULL, 9780504ULL, 1795265022ULL}
    };
    if (n < 7999252175582851ULL) {
      if (n < 350269456337ULL) {
        if (n < 4294967296ULL) {
          return isPrime(static_cast<uint32_t>(n));
        } else {
          return isSprp(n, bases[0]);
        }
      } else {
        if (n < 55245642489451ULL) {
          return isSprp(n, bases[1]);
        } else {
          return isSprp(n, bases[2]);
        }
      }
    } else {
      if (n < 585226005592931977ULL) {
        return isSprp(n, bases[3]);
      } else {
        return isSprp(n, bases[4]);
      }
    }
  }

  bool isPrime(int64_t n) {
    return isPrime(static_cast<uint64_t>(n));
  }
  //@}

  /// @} number_theory
}  // namespace algo

#define F first
#define S second
#define ALL(x) (x).begin(), (x).end()

using namespace std;
using namespace algo;

typedef long double dbl;

namespace task {
  int t, n, k;
  dbl p, u, r;

  int main() {
    cin >> t;
    for (int i = 0; i < t; ++i) {
      priority_queue<dbl, vector<dbl>, greater<dbl>> q;
      cin >> n >> k >> u;
      for (int j = 0; j < n; ++j) {
        cin >> p;
        q.push(p);
      }
      while (u > EPS) {
        dbl tmp = q.top();
        q.pop();
        tmp += 0.0001L;
        u -= 0.0001L;
        q.push(tmp);
      }
      r = 1.0L;
      while (!q.empty()) {
        r *= q.top();
        q.pop();
      }
      cout << "Case #" << i + 1 << ": " << r << '\n';
    }
    return 0;
  }
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.precision(11);
  cout.setf(ios::fixed);
#ifdef _DEBUG
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#elif defined(TASK)
  freopen(TASK".in", "r", stdin);
  freopen(TASK".out", "w", stdout);
#endif
  return task::main();
}
