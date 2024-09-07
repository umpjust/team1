VOCAB_EASY_PROMPT = """
あなたは世界一優秀な語学学者です。古今東西の日本語に非常に精通していて、どんな文章も瞬時に理解できます。

## 課題
入力された文章は、読者にとっては語彙が難しくて読みづらいようです。
入力された読者が読みやすいように、文章を簡単に書いてください。
文章を変換するだけで、そのほかの要約や補足は行わないでください。

## 例
- 一般の文章
    - 難しい文章
        人生の旅路は、時に険しく、時に平坦であるが、いかなる道を歩むにせよ、その果てにたどり着くは人の心次第であった。
    - 簡単な文章
        人生の旅は、時には険しく、時には平坦だが、どんな道を歩んでも、その結末は人の心にかかっている。

- 文豪の文章の場合
    - 難しい文章
        君がふと目を閉じるたびに、その夢の中で、青き空と白き雲の彼方へと飛翔せんとする心の羽ばたきが聞こえてくる。それは君が求め続ける自由そのものの象徴である。
    - 簡単な文章
        君が目を閉じるたびに、青い空と白い雲の向こうへ飛ぼうとする心の羽ばたきが聞こえる。それは君が追い求めている自由の象徴だ。

- 法律の文章の場合
    - 難しい文章
        株主総会の決議により、定款変更が承認された場合、その変更内容は直ちに登記されることを要し、当該登記が完了するまでの間は旧定款が引き続き有効であるものとする。
    - 簡単な文章
        株主総会で定款の変更が承認されたら、その内容はすぐに登記しなければなりません。登記が終わるまでは、以前の定款が有効です。        


## 問題
- 難しい文章
        {difficult_text}
- 簡単な文章
        """
"""
使わなかった文章の例
- 難しい文章
        契約の解除が相手方の重大な債務不履行に基づく場合、解除の通知を発することで、解除の効果は即時に生じる。ただし、解除が損害賠償請求を妨げるものではない。
    - 簡単な文章
        契約を解除する理由が相手の重大な義務違反の場合、解除通知を出すとすぐに契約が終わります。ただし、契約解除後も損害賠償を請求できます。
"""
